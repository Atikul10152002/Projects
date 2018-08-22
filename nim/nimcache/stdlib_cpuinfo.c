/* Generated by Nim Compiler v0.18.0 */
/*   (c) 2018 Andreas Rumpf */
/* The generated code is subject to the original license. */
/* Compiled for: MacOSX, amd64, clang */
/* Command for C compiler:
   clang -c  -w  -I/Users/atikul/.choosenim/toolchains/nim-0.18.0/lib -o /Users/atikul/GitHub/projects/nim/nimcache/stdlib_cpuinfo.o /Users/atikul/GitHub/projects/nim/nimcache/stdlib_cpuinfo.c */
#define NIM_NEW_MANGLING_RULES
#define NIM_INTBITS 64

#include "nimbase.h"
#include <string.h>
#undef LANGUAGE_C
#undef MIPSEB
#undef MIPSEL
#undef PPC
#undef R3000
#undef R4000
#undef i386
#undef linux
#undef mips
#undef near
#undef powerpc
#undef unix
typedef int tyArray_VR9bNthWayFgb5M9avIR8bkA[4];
#include <sys/types.h>
#include <sys/sysctl.h>
N_LIB_PRIVATE N_NIMCALL(NI, ncpicountProcessors)(void);
static N_INLINE(void, nimFrame)(TFrame* s);
N_LIB_PRIVATE N_NOINLINE(void, stackOverflow_II46IjNZztN9bmbxUD8dt8g)(void);
static N_INLINE(void, popFrame)(void);
extern TFrame* framePtr_HRfVMH3jYeBJz6Q6X9b6Ptw;

static N_INLINE(void, nimFrame)(TFrame* s) {
	NI T1_;
	T1_ = (NI)0;
	{
		if (!(framePtr_HRfVMH3jYeBJz6Q6X9b6Ptw == NIM_NIL)) goto LA4_;
		T1_ = ((NI) 0);
	}
	goto LA2_;
	LA4_: ;
	{
		T1_ = ((NI) ((NI16)((*framePtr_HRfVMH3jYeBJz6Q6X9b6Ptw).calldepth + ((NI16) 1))));
	}
	LA2_: ;
	(*s).calldepth = ((NI16) (T1_));
	(*s).prev = framePtr_HRfVMH3jYeBJz6Q6X9b6Ptw;
	framePtr_HRfVMH3jYeBJz6Q6X9b6Ptw = s;
	{
		if (!((*s).calldepth == ((NI16) 2000))) goto LA9_;
		stackOverflow_II46IjNZztN9bmbxUD8dt8g();
	}
	LA9_: ;
}

static N_INLINE(void, popFrame)(void) {
	framePtr_HRfVMH3jYeBJz6Q6X9b6Ptw = (*framePtr_HRfVMH3jYeBJz6Q6X9b6Ptw).prev;
}

N_LIB_PRIVATE N_NIMCALL(NI, ncpicountProcessors)(void) {
	NI result;
	tyArray_VR9bNthWayFgb5M9avIR8bkA mib;
	NI numCPU;
	size_t len;
	int T1_;
	nimfr_("countProcessors", "cpuinfo.nim");
	result = (NI)0;
	memset((void*)mib, 0, sizeof(mib));
	numCPU = (NI)0;
	len = (size_t)0;
	nimln_(72, "cpuinfo.nim");
	mib[(((NI) 0))- 0] = ((int) 6);
	nimln_(73, "cpuinfo.nim");
	mib[(((NI) 1))- 0] = ((int) 25);
	nimln_(74, "cpuinfo.nim");
	len = ((NI) 8);
	nimln_(75, "cpuinfo.nim");
	T1_ = (int)0;
	T1_ = sysctl(mib, ((int) 2), ((void*) ((&numCPU))), (&len), NIM_NIL, ((NI) 0));
	T1_;
	nimln_(76, "cpuinfo.nim");
	{
		int T6_;
		if (!(numCPU < ((NI) 1))) goto LA4_;
		nimln_(77, "cpuinfo.nim");
		mib[(((NI) 1))- 0] = ((int) 3);
		nimln_(78, "cpuinfo.nim");
		T6_ = (int)0;
		T6_ = sysctl(mib, ((int) 2), ((void*) ((&numCPU))), (&len), NIM_NIL, ((NI) 0));
		T6_;
	}
	LA4_: ;
	nimln_(79, "cpuinfo.nim");
	result = numCPU;
	nimln_(89, "cpuinfo.nim");
	{
		if (!(result <= ((NI) 0))) goto LA9_;
		result = ((NI) 0);
	}
	LA9_: ;
	popFrame();
	return result;
}
NIM_EXTERNC N_NOINLINE(void, stdlib_cpuinfoInit000)(void) {
	nimfr_("cpuinfo", "cpuinfo.nim");
	popFrame();
}

NIM_EXTERNC N_NOINLINE(void, stdlib_cpuinfoDatInit000)(void) {
}

