
clear

// (*Time and nodes*)
 nodesperlayer = 3; // Should be 2 or more, 3 is good.
 layertime = 200; // Physical time between deposition of each new layer(seconds)
// layertime = [10 40 70 100 120 150 200 250 300 375 450 600];
 cooldowntime = 30; // seconds
 timeskip = 1;

 w = 0.02; // wall thickness(m)
 layer = 0.004064; // layer height(m)
 layers = 10;

 //(*Material properties*)
 alpha = 2.0*10 ^ (-7); // thermal diffusivity
 c = 1640; // specific heat(J/kg.K)
 rho = 1140; // density(kg/m ^ 3)
 k = 0.17; // thermal conductivity(W/m.K)
 u = 0.15 // Temp increase per second(This is a total klooge, but shows how const. heat gen can be added)
 counter1 = 1;
 counter2 = 1;

 Tdep = 200 + 273; // Deposition temperature(K)
 Tb = 65 + 273; // Build plate temperature(K)
 Tinf = 18 + 273; // Ambient temperature(K)
 h = 8.50; // Natural convection coefficient(W/m ^ 2.K)

 emissivity = 0.87;

function[Tss, delx, delt, timepoints, cooldowntimepoints, spatialdataplot, timedataplot, timeskip] = buildwall(
    nodesperlayer, w, layers, layer, layertime, cooldowntime, alpha, c, rho, k, Tdep, Tinf, Tb, h, emissivity, counter1, counter2, u)

 // Build the wall
 for n = 1: layers

//Solve for temperature
   //Iterate in time, j
   for j = ((n-1)*timepoints + 1): (n*timepoints + temporary)
// (*Bottom node with constant temperature BC*)
    hrad = emissivity*sigma*(Tnodes(j, 1) + Tinf) * \
                             (Tnodes(j, 1) ^ 2 + Tinf ^ 2);

    Qcond = k*w/delx*(Tnodes(j, 1 + 1) + 2*Tb - 3*Tnodes(j, 1));
    Qconv = 1*h*delx*(Tinf - Tnodes(j, 1));
    Qrad = 1*hrad*delx*(Tinf - Tnodes(j, 1));

    Qbed(j+1) = 2*k*w/delx*(Tb-Tnodes(j, 1));
    Qwall(j+1) = Qconv+Qrad;

    // Here is where the temperature is calculated for the current node at the next time increment.
// Tnodes(j+1, 1) = (2*delt/(rho*c*delx*w))*(Qcond+Qconv+Qrad)+Tnodes(j, 1);
    Tnodes(j+1, 1) = (2*delt/(rho*c*delx*w))*(Qcond+Qconv+Qrad)+Tnodes(j, 1) + u*delt;

    Qcond_sum = 0;
    Qconv_sum = 0;
    Qrad_sum = 0;

// (*Middle nodes with convective cooling and conduction*)
    //Iterate through nodes, i
    for i = 2: n*nodesperlayer-1
     hrad = emissivity*sigma*(Tnodes(j, i) + Tinf) * \
                              (Tnodes(j, i) ^ 2 + Tinf ^ 2);

     Qcond = k*w/delx*(Tnodes(j, i + 1) + Tnodes(j, i - 1) - 2*Tnodes(j, i));
     Qconv = 2*h*delx*(Tinf - Tnodes(j, i));
     Qrad = 2*hrad*delx*(Tinf - Tnodes(j, i));

     Qcond_sum = Qcond_sum + Qcond;
     Qconv_sum = Qconv_sum + Qconv;
     Qrad_sum = Qrad_sum + Qrad;

    // Here is where the temperature is calculated for the current node at the next time increment.
// Tnodes(j+1, i) = (delt/(rho*c*delx*w))*(Qcond+Qconv+Qrad) + Tnodes(j, i);
     Tnodes(j+1, i) = (delt/(rho*c*delx*w))*(Qcond+Qconv+Qrad) + Tnodes(j, i) + u*delt;

	end;

    Qwall(j+1) = Qwall(j+1) + Qconv_sum + Qrad_sum;

    //(*Top node with convective cooling on 3 sides and conduction from below*)
    hrad = emissivity*sigma*(Tnodes(j, (n-0)*nodesperlayer) + Tinf)*(Tnodes(j, (n-0)*nodesperlayer)^2 + Tinf^2);

    Qcond = k*w/delx*(Tnodes(j, n*nodesperlayer - 1) - Tnodes(j, n*nodesperlayer));
    Qconv = 1*h*delx*(Tinf - Tnodes(j, n*nodesperlayer)) + h*w*(Tinf-Tnodes(j,n*nodesperlayer));
    Qrad = 1*hrad*delx*(Tinf - Tnodes(j, n*nodesperlayer)) + hrad*w*(Tinf-Tnodes(j,n*nodesperlayer));

    Qtop(j+1) = Qconv + Qrad;

    // Here is where the temperature is calculated for the current node at the next time increment.
//    Tnodes(j+1,n*nodesperlayer)= (2*delt/(rho*c*delx*w))*(Qcond+Qconv+Qrad)+ Tnodes(j, n*nodesperlayer);
    Tnodes(j+1,n*nodesperlayer)= (2*delt/(rho*c*delx*w))*(Qcond+Qconv+Qrad)+ Tnodes(j, n*nodesperlayer) + u*delt;

    if j==n*timepoints then
        Tsubstrate(n) = Tnodes(j+1,n*nodesperlayer-1);
    end
  end;

  end;

 Tnodes = Tnodes-273;
 Tnodes(find(Tnodes==200)) = -10;
 Tss = Tnodes((layers-1)*timepoints+1,(layers-1)*nodesperlayer-floor(nodesperlayer/2));

 timedataplot = Tnodes(1:timeskip:(timepoints*layers+cooldowntimepoints+1),2:nodesperlayer:nodesperlayer*layers);
 x = [delx:delx:layers*nodesperlayer*delx];

 layerskip=2;
 cooldownplotinc = 600; //seconds (10 minutes)
 temp = floor(cooldownplotinc/delt);

spatialdataplot = Tnodes([(layerskip-1)*timepoints:layerskip*timepoints:timepoints*(layers-1) (timepoints*layers):temp:(timepoints*layers+cooldowntimepoints+0)],:)';

endfunction;

//------------------------------------------------
// Run function
//------------------------------------------------

for i = 1:length(w)
    for j = 1:length(layertime)
        [Tss,delx,delt,timepoints,cooldowntimepoints,spatialdataplot,timedataplot] = buildwall(nodesperlayer,w(i),layers,layer,layertime(j),cooldowntime,alpha,c,rho,k,Tdep,Tinf,Tb,h,emissivity,counter1,counter2);
        steady_state(i,j) = Tss;
        spatial_data_plot(:,:,j) = spatialdataplot;
//        time_data_plot(:,:,j) = timedataplot;
        counter1 = counter1 + 1;

        x = [delx:delx:layers*nodesperlayer*delx]';
//        clf(0);
//        f=figure(0)
//        f.background = -2
//        plot(x,steady_state,'g-')
//        xlabel("Position (m)","fontsize",4)
//        ylabel("Temperature (C)","fontsize",4)
//        a = get("current_axes")
//        a.data_bounds=[0,0;0.4,200];
//        a.font_size=3

        time = [0:timeskip*delt:(layers*timepoints+cooldowntimepoints)*delt]';

        clf(1);
        f=figure(1)
        f.background = -2
//        plot(time./60,timedataplot(:,1),'-')
        plot(time./60,timedataplot,'d')
        xlabel("Time (min)","fontsize",4)
        ylabel("Temperature (C)","fontsize",4)
        b = get("current_axes")
//        b.data_bounds=[0,(Tb(j)-273-10);15,(Tb(j)-273+30)];
        b.data_bounds=[0,0;40,200];
//        b.font_size=3
    end
    counter2 = counter2 + 1;
    counter1 = 1;
end
//------------------------------------------------
// End function call
//------------------------------------------------

//        f=figure(2)
//        f.background = -2
//        plot(layertime,steady_state,'-o')
//        xlabel("Layertime (s)","fontsize",4)
//        ylabel("Temperature (C)","fontsize",4)
//        a = get("current_axes")
//        a.data_bounds=[0,0;600,200];
//        a.font_size=3
//        xs2pdf(0,strcat(['C:\Users\bcompto1\Dropbox\ORNL\Thermomechanical modeling paper\fixed_model\steady_state_w_h8p5.pdf']))
