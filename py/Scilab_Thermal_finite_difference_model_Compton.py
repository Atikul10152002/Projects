# ---------------------------------------------------------------------
# A 1D thermal model for large-scale polymer AM. Brett G. Compton, PhD
# ---------------------------------------------------------------------

import math

import matplotlib.pyplot as plt
import numpy as np

# (*Time and nodes*)
nodesperlayer = 3  # Should be 2 or more, 3 is good.
# Physical time between deposition of each new layer (seconds)
layertime = [200]
# layertime = [10 40 70 100 120 150 200 250 300 375 450 600]
cooldowntime = 30          # seconds
timeskip = 1

w = [0.02]                   # wall thickness (m)
layer = 0.004064           # layer height (m)
layers = 10

# (*Material properties*)
alpha = 2.0*10**(-7)       # thermal diffusivity
c = 1640                   # specific heat (J/kg.K)
rho = 1140                 # density (kg/m**3)
k = 0.17                   # thermal conductivity (W/m.K)
# Temp increase per second (This is a total klooge, but shows how const. heat gen can be added)
u = 0.15
counter1 = 1
counter2 = 1

Tdep = 200 + 273           # Deposition temperature (K)
Tb = 65 + 273              # Build plate temperature (K)
Tinf = 18 + 273            # Ambient temperature (K)
h = 8.50                   # Natural convection coefficient (W/m**2.K)

emissivity = 0.87


def buildwall(nodesperlayer, w, layers, layer, layertime, cooldowntime, alpha, c, rho, k, Tdep, Tinf, Tb, h, emissivity, counter1, counter2, u):
    # (*Geometry*)
    thick = math.floor(w*1000)
    height = layers*layer

    # (*Thermal details*)
    sigma = 5.670*10**(-8)
    hradmax = emissivity*sigma*(Tdep + Tinf)*(Tdep ** 2 + Tinf ** 2)

    delx = layer/nodesperlayer
    nodes = list(range(1, nodesperlayer+1))

    deltmaxbot = (12*k/(rho*c*delx ** 2) + 2*(h+hradmax)/(rho*c*w)) ** (-1)
    deltmaxtop = (2*k/(rho*c*delx**2) + 2*(h + hradmax) /
                  (rho*c*w) + 2*(h + hradmax)/(rho*c*delx))**(-1)

    delt = min(deltmaxbot, deltmaxtop)
    timefactor = 0.75
    delt = timefactor*delt

    Bi = h*delx/k                   # Biot number
    Fo = k*delt/(rho*c*delx**2)     # Fourier number

    Tsubstrate = np.empty((0, 1), np.float)

    timepoints = math.floor(layertime/delt) + 1
    delt = layertime/timepoints
    cooldowntimepoints = math.floor(cooldowntime/delt)
    temporary = 0

    Qcond_sum = 0
    Qconv_sum = 0
    Qrad_sum = 0

    # Initialize nodal matrix
    Tnodes = np.zeros(
        (timepoints*layers+cooldowntimepoints, nodesperlayer*layers))
    Qtop = np.zeros((timepoints*layers+cooldowntimepoints, 1))
    Qwall = np.zeros((timepoints*layers+cooldowntimepoints, 1))
    Qbed = np.zeros((timepoints*layers+cooldowntimepoints, 1))

    # Build the wall
    for n in range(1, layers+1):
        if n == 1:
            Tnodes[0, 0:nodesperlayer] = Tdep
        elif n == layers:
            temporary = cooldowntimepoints
            Tnodes[((n-1)*timepoints), (n-1) *
                   nodesperlayer:n*nodesperlayer] = Tdep
        else:
            Tnodes[((n-1)*timepoints), (n-1) *
                   nodesperlayer:n*nodesperlayer] = Tdep

        #Solve for temperature
        #Iterate in time, j
        for j in range((n-1)*timepoints+1, n*timepoints + temporary+1):
            hrad = emissivity*sigma * \
                (Tnodes[j-1, 0] + Tinf)*(Tnodes[j-1, 0] ** 2 + Tinf ** 2)
            Qcond = k*w/delx*(Tnodes[j-1, 1] + 2*Tb - 3*Tnodes[j-1, 0])
            Qconv = 1*h*delx*(Tinf - Tnodes[j-1, 0])
            Qrad = 1*hrad*delx*(Tinf - Tnodes[j-1, 0])

            if j == Qbed.shape[0]:
                Qbed = np.vstack([Qbed, np.zeros((1, Qbed.shape[1]))])
            if j == Qwall.shape[0]:
                Qwall = np.vstack([Qwall, np.zeros((1, Qwall.shape[1]))])
            if j == Qtop.shape[0]:
                Qtop = np.vstack([Qtop, np.zeros((1, Qtop.shape[1]))])
            if j == Tnodes.shape[0]:
                Tnodes = np.vstack([Tnodes, np.zeros((1, Tnodes.shape[1]))])

            Qbed[j] = 2*k*w/delx*(Tb-Tnodes[j-1, 0])
            Qwall[j] = Qconv+Qrad

            # Here is where the temperature is calculated for the current node at the next time increment.
            Tnodes[j, 0] = (2*delt/(rho*c*delx*w)) * \
                (Qcond+Qconv+Qrad)+Tnodes[j-1, 0] + u*delt

            Qcond_sum = 0
            Qconv_sum = 0
            Qrad_sum = 0

            # (*Middle nodes with convective cooling and conduction*)
            # Iterate through nodes, i

            for i in range(2, n*nodesperlayer):
                hrad = emissivity*sigma * \
                    (Tnodes[j-1, i-1] + Tinf)*(Tnodes[j-1, i-1]**2 + Tinf**2)
                Qcond = k*w/delx*(Tnodes[j-1, i] +
                                  Tnodes[j-1, i - 2] - 2*Tnodes[j-1, i-1])
                Qconv = 2*h*delx*(Tinf - Tnodes[j-1, i-1])
                Qrad = 2*hrad*delx*(Tinf - Tnodes[j-1, i-1])

                Qcond_sum = Qcond_sum + Qcond
                Qconv_sum = Qconv_sum + Qconv
                Qrad_sum = Qrad_sum + Qrad

                # Here is where the temperature is calculated for the current node at the next time increment.
                # Tnodes(j+1,i)= (delt/(rho*c*delx*w))*(Qcond+Qconv+Qrad) + Tnodes(j, i);
                Tnodes[j, i-1] = (delt/(rho*c*delx*w)) * \
                    (Qcond+Qconv+Qrad) + Tnodes[j-1, i-1] + u*delt

            Qwall[j] = Qwall[j] + Qconv_sum + Qrad_sum

            # (*Top node with convective cooling on 3 sides and conduction from below*)
            hrad = emissivity*sigma*(Tnodes[j-1, (n-0)*nodesperlayer-1] + Tinf) * \
                (Tnodes[j-1, (n-0)*nodesperlayer-1] ** 2 + Tinf ** 2)

            Qcond = k*w/delx*(Tnodes[j-1, n*nodesperlayer - 2] -
                              Tnodes[j-1, n*nodesperlayer-1])
            Qconv = 1*h*delx*(Tinf - Tnodes[j-1, n*nodesperlayer-1]) + \
                h*w*(Tinf-Tnodes[j-1, n*nodesperlayer-1])
            Qrad = 1*hrad*delx*(Tinf - Tnodes[j-1, n*nodesperlayer-1]) + \
                hrad*w*(Tinf-Tnodes[j-1, n*nodesperlayer-1])

            Qtop[j] = Qconv + Qrad

            # Here is where the temperature is calculated for the current node at the next time increment.

            # Tnodes(j+1, n*nodesperlayer) = (2*delt/(rho*c*delx*w))*(Qcond+Qconv+Qrad) + Tnodes(j, n*nodesperlayer)
            Tnodes[j, n*nodesperlayer-1] = (2*delt/(rho*c*delx*w))*(
                Qcond+Qconv+Qrad) + Tnodes[j-1, n*nodesperlayer-1] + u*delt

            if j == n*timepoints:
                Tsubstrate = np.append(Tsubstrate, np.array(
                    [[Tnodes[j, n*nodesperlayer-2]]]), axis=0)

    Tnodes = Tnodes-273
    Tnodes[np.where(Tnodes == 200)] = -10
    Tss = Tnodes[(layers-1)*timepoints, (layers-1) *
                 nodesperlayer-math.floor(nodesperlayer/2)-1]

    timedataplot = Tnodes[0:(timepoints*layers+cooldowntimepoints+1)
                             :timeskip, 1:nodesperlayer*layers:nodesperlayer]
    x = np.arange(delx, (layers*nodesperlayer*delx)+10**-10, delx)

    layerskip = 2
    cooldownplotinc = 600  # seconds (10 minutes)
    temp = math.floor(cooldownplotinc/delt)

    spatialdataplot = np.swapaxes(
        Tnodes[np.concatenate(
            [np.arange(
                (layerskip-1)*timepoints,
                timepoints * (layers-1)+10**-10,
                layerskip * timepoints,
                dtype=np.int)-1,
             np.arange(
                (timepoints*layers),
                (timepoints * layers+cooldowntimepoints+0),
                temp+10**-5,
                dtype=np.int)-1
             ], axis=0), :], 0, 1)
    return Tss, delx, delt, timepoints, cooldowntimepoints, spatialdataplot, timedataplot, timeskip


# ------------------------------------------------
# Run function
# ------------------------------------------------
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel("Time (min)")
ax.set_ylabel("Temperature (C)")

for i in range(1, len(w)+1):
    for j in range(1, len(layertime)+1):
        Tss, delx, delt, timepoints, cooldowntimepoints, spatialdataplot, timedataplot, timeskip = buildwall(
            nodesperlayer, w[i-1], layers, layer, layertime[j-1], cooldowntime, alpha, c, rho, k, Tdep, Tinf, Tb, h, emissivity, counter1, counter2, u)

        # steady_state[i-1, j-1] = Tss
        # spatial_data_plot[:, :, j] = spatialdataplot
        # time_data_plot(:,:,j) = timedataplot;
        counter1 = counter1 + 1

        x = np.arange(delx, (layers*nodesperlayer*delx)+10**-10, delx)

        time = np.arange(
            0, ((layers*timepoints+cooldowntimepoints)*delt)+10**-10, timeskip*delt)
        ax.clear()
        # ax.set_xlim([0,40])
        # ax.set_ylim([-200,200])
        for i in range(timedataplot.shape[1]):
            ax.scatter(np.divide(time, 60),
                       timedataplot[:, i], marker='s')
        fig.savefig(f'3d-print-layer{str(i)+str(j)}.png')

    counter2 += 1
    counter1 = 1

# plt.show()

#------------------------------------------------
# End function call
#------------------------------------------------
