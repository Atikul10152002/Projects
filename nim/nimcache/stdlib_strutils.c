/* Generated by Nim Compiler v0.18.0 */
/*   (c) 2018 Andreas Rumpf */
/* The generated code is subject to the original license. */
/* Compiled for: MacOSX, amd64, clang */
/* Command for C compiler:
   clang -c  -w  -I/Users/atikul/.choosenim/toolchains/nim-0.18.0/lib -o /Users/atikul/GitHub/projects/nim/nimcache/stdlib_strutils.o /Users/atikul/GitHub/projects/nim/nimcache/stdlib_strutils.c */
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
typedef struct NimStringDesc NimStringDesc;
typedef struct TGenericSeq TGenericSeq;
typedef struct tyObject_HSlice_x7qpDivRIi6zcMSMsudNPA tyObject_HSlice_x7qpDivRIi6zcMSMsudNPA;
typedef struct tyObject_HSlice_lKy9cDUCgy9ap43jXru18mYw tyObject_HSlice_lKy9cDUCgy9ap43jXru18mYw;
typedef struct tyObject_ValueError_Gi06FkNeykJn7mrqRZYrkA tyObject_ValueError_Gi06FkNeykJn7mrqRZYrkA;
typedef struct Exception Exception;
typedef struct RootObj RootObj;
typedef struct TNimType TNimType;
typedef struct TNimNode TNimNode;
typedef struct tySequence_uB9b75OUPRENsBAu4AnoePA tySequence_uB9b75OUPRENsBAu4AnoePA;
typedef struct tyObject_Cell_1zcF9cV8XIAtbN8h5HRUB8g tyObject_Cell_1zcF9cV8XIAtbN8h5HRUB8g;
typedef struct tyObject_CellSeq_Axo1XVm9aaQueTOldv8le5w tyObject_CellSeq_Axo1XVm9aaQueTOldv8le5w;
typedef struct tyObject_GcHeap_1TRH1TZMaVZTnLNcIHuNFQ tyObject_GcHeap_1TRH1TZMaVZTnLNcIHuNFQ;
typedef struct tyObject_GcStack_7fytPA5bBsob6See21YMRA tyObject_GcStack_7fytPA5bBsob6See21YMRA;
typedef struct tyObject_MemRegion_x81NhDv59b8ercDZ9bi85jyg tyObject_MemRegion_x81NhDv59b8ercDZ9bi85jyg;
typedef struct tyObject_SmallChunk_tXn60W2f8h3jgAYdEmy5NQ tyObject_SmallChunk_tXn60W2f8h3jgAYdEmy5NQ;
typedef struct tyObject_BigChunk_Rv9c70Uhp2TytkX7eH78qEg tyObject_BigChunk_Rv9c70Uhp2TytkX7eH78qEg;
typedef struct tyObject_LLChunk_XsENErzHIZV9bhvyJx56wGw tyObject_LLChunk_XsENErzHIZV9bhvyJx56wGw;
typedef struct tyObject_IntSet_EZObFrE3NC9bIb3YMkY9crZA tyObject_IntSet_EZObFrE3NC9bIb3YMkY9crZA;
typedef struct tyObject_Trunk_W0r8S0Y3UGke6T9bIUWnnuw tyObject_Trunk_W0r8S0Y3UGke6T9bIUWnnuw;
typedef struct tyObject_AvlNode_IaqjtwKhxLEpvDS9bct9blEw tyObject_AvlNode_IaqjtwKhxLEpvDS9bct9blEw;
typedef struct tyObject_HeapLinks_PDV1HBZ8CQSQJC9aOBFNRSg tyObject_HeapLinks_PDV1HBZ8CQSQJC9aOBFNRSg;
typedef struct tyTuple_ujsjpB2O9cjj3uDHsXbnSzg tyTuple_ujsjpB2O9cjj3uDHsXbnSzg;
typedef struct tyObject_GcStat_0RwLoVBHZPfUAcLczmfQAg tyObject_GcStat_0RwLoVBHZPfUAcLczmfQAg;
typedef struct tyObject_CellSet_jG87P0AI9aZtss9ccTYBIISQ tyObject_CellSet_jG87P0AI9aZtss9ccTYBIISQ;
typedef struct tyObject_PageDesc_fublkgIY4LG3mT51LU2WHg tyObject_PageDesc_fublkgIY4LG3mT51LU2WHg;
typedef struct tyObject_StackTraceEntry_oLyohQ7O2XOvGnflOss8EA tyObject_StackTraceEntry_oLyohQ7O2XOvGnflOss8EA;
typedef struct tyObject_BaseChunk_Sdq7WpT6qAH858F5ZEdG3w tyObject_BaseChunk_Sdq7WpT6qAH858F5ZEdG3w;
typedef struct tyObject_FreeCell_u6M5LHprqzkn9axr04yg9bGQ tyObject_FreeCell_u6M5LHprqzkn9axr04yg9bGQ;
struct TGenericSeq {
NI len;
NI reserved;
};
struct NimStringDesc {
  TGenericSeq Sup;
NIM_CHAR data[SEQ_DECL_SIZE];
};
struct tyObject_HSlice_x7qpDivRIi6zcMSMsudNPA {
NI a;
NI b;
};
struct tyObject_HSlice_lKy9cDUCgy9ap43jXru18mYw {
NI a;
NI b;
};
typedef NU8 tyEnum_TNimKind_jIBKr1ejBgsfM33Kxw4j7A;
typedef NU8 tySet_tyEnum_TNimTypeFlag_v8QUszD1sWlSIWZz7mC4bQ;
typedef N_NIMCALL_PTR(void, tyProc_ojoeKfW4VYIm36I9cpDTQIg) (void* p, NI op);
typedef N_NIMCALL_PTR(void*, tyProc_WSm2xU5ARYv9aAR4l0z9c9auQ) (void* p);
struct TNimType {
NI size;
tyEnum_TNimKind_jIBKr1ejBgsfM33Kxw4j7A kind;
tySet_tyEnum_TNimTypeFlag_v8QUszD1sWlSIWZz7mC4bQ flags;
TNimType* base;
TNimNode* node;
void* finalizer;
tyProc_ojoeKfW4VYIm36I9cpDTQIg marker;
tyProc_WSm2xU5ARYv9aAR4l0z9c9auQ deepcopy;
};
struct RootObj {
TNimType* m_type;
};
struct Exception {
  RootObj Sup;
Exception* parent;
NCSTRING name;
NimStringDesc* message;
tySequence_uB9b75OUPRENsBAu4AnoePA* trace;
Exception* up;
};
struct tyObject_ValueError_Gi06FkNeykJn7mrqRZYrkA {
  Exception Sup;
};
typedef NU8 tyEnum_TNimNodeKind_unfNsxrcATrufDZmpBq4HQ;
struct TNimNode {
tyEnum_TNimNodeKind_unfNsxrcATrufDZmpBq4HQ kind;
NI offset;
TNimType* typ;
NCSTRING name;
NI len;
TNimNode** sons;
};
struct tyObject_Cell_1zcF9cV8XIAtbN8h5HRUB8g {
NI refcount;
TNimType* typ;
};
struct tyObject_GcStack_7fytPA5bBsob6See21YMRA {
void* bottom;
};
struct tyObject_CellSeq_Axo1XVm9aaQueTOldv8le5w {
NI len;
NI cap;
tyObject_Cell_1zcF9cV8XIAtbN8h5HRUB8g** d;
};
typedef tyObject_SmallChunk_tXn60W2f8h3jgAYdEmy5NQ* tyArray_SiRwrEKZdLgxqz9a9aoVBglg[512];
typedef NU32 tyArray_BHbOSqU1t9b3Gt7K2c6fQig[24];
typedef tyObject_BigChunk_Rv9c70Uhp2TytkX7eH78qEg* tyArray_N1u1nqOgmuJN9cSZrnMHgOQ[32];
typedef tyArray_N1u1nqOgmuJN9cSZrnMHgOQ tyArray_B6durA4ZCi1xjJvRtyYxMg[24];
typedef tyObject_Trunk_W0r8S0Y3UGke6T9bIUWnnuw* tyArray_lh2A89ahMmYg9bCmpVaplLbA[256];
struct tyObject_IntSet_EZObFrE3NC9bIb3YMkY9crZA {
tyArray_lh2A89ahMmYg9bCmpVaplLbA data;
};
typedef tyObject_AvlNode_IaqjtwKhxLEpvDS9bct9blEw* tyArray_0aOLqZchNi8nWtMTi8ND8w[2];
struct tyObject_AvlNode_IaqjtwKhxLEpvDS9bct9blEw {
tyArray_0aOLqZchNi8nWtMTi8ND8w link;
NI key;
NI upperBound;
NI level;
};
struct tyTuple_ujsjpB2O9cjj3uDHsXbnSzg {
tyObject_BigChunk_Rv9c70Uhp2TytkX7eH78qEg* Field0;
NI Field1;
};
typedef tyTuple_ujsjpB2O9cjj3uDHsXbnSzg tyArray_LzOv2eCDGiceMKQstCLmhw[30];
struct tyObject_HeapLinks_PDV1HBZ8CQSQJC9aOBFNRSg {
NI len;
tyArray_LzOv2eCDGiceMKQstCLmhw chunks;
tyObject_HeapLinks_PDV1HBZ8CQSQJC9aOBFNRSg* next;
};
struct tyObject_MemRegion_x81NhDv59b8ercDZ9bi85jyg {
NI minLargeObj;
NI maxLargeObj;
tyArray_SiRwrEKZdLgxqz9a9aoVBglg freeSmallChunks;
NU32 flBitmap;
tyArray_BHbOSqU1t9b3Gt7K2c6fQig slBitmap;
tyArray_B6durA4ZCi1xjJvRtyYxMg matrix;
tyObject_LLChunk_XsENErzHIZV9bhvyJx56wGw* llmem;
NI currMem;
NI maxMem;
NI freeMem;
NI occ;
NI lastSize;
tyObject_IntSet_EZObFrE3NC9bIb3YMkY9crZA chunkStarts;
tyObject_AvlNode_IaqjtwKhxLEpvDS9bct9blEw* root;
tyObject_AvlNode_IaqjtwKhxLEpvDS9bct9blEw* deleted;
tyObject_AvlNode_IaqjtwKhxLEpvDS9bct9blEw* last;
tyObject_AvlNode_IaqjtwKhxLEpvDS9bct9blEw* freeAvlNodes;
NIM_BOOL locked;
NIM_BOOL blockChunkSizeIncrease;
NI nextChunkSize;
tyObject_AvlNode_IaqjtwKhxLEpvDS9bct9blEw bottomData;
tyObject_HeapLinks_PDV1HBZ8CQSQJC9aOBFNRSg heapLinks;
};
struct tyObject_GcStat_0RwLoVBHZPfUAcLczmfQAg {
NI stackScans;
NI cycleCollections;
NI maxThreshold;
NI maxStackSize;
NI maxStackCells;
NI cycleTableSize;
NI64 maxPause;
};
struct tyObject_CellSet_jG87P0AI9aZtss9ccTYBIISQ {
NI counter;
NI max;
tyObject_PageDesc_fublkgIY4LG3mT51LU2WHg* head;
tyObject_PageDesc_fublkgIY4LG3mT51LU2WHg** data;
};
struct tyObject_GcHeap_1TRH1TZMaVZTnLNcIHuNFQ {
tyObject_GcStack_7fytPA5bBsob6See21YMRA stack;
NI cycleThreshold;
tyObject_CellSeq_Axo1XVm9aaQueTOldv8le5w zct;
tyObject_CellSeq_Axo1XVm9aaQueTOldv8le5w decStack;
tyObject_CellSeq_Axo1XVm9aaQueTOldv8le5w tempStack;
NI recGcLock;
tyObject_MemRegion_x81NhDv59b8ercDZ9bi85jyg region;
tyObject_GcStat_0RwLoVBHZPfUAcLczmfQAg stat;
tyObject_CellSet_jG87P0AI9aZtss9ccTYBIISQ marked;
tyObject_CellSeq_Axo1XVm9aaQueTOldv8le5w additionalRoots;
NI gcThreadId;
};
typedef NU8 tySet_tyChar_nmiMWKVIe46vacnhAFrQvw[32];
typedef NI tyArray_9cc9aPiDa8VaWjVcFLabEDZQ[256];
struct tyObject_StackTraceEntry_oLyohQ7O2XOvGnflOss8EA {
NCSTRING procname;
NI line;
NCSTRING filename;
};
struct tyObject_BaseChunk_Sdq7WpT6qAH858F5ZEdG3w {
NI prevSize;
NI size;
};
struct tyObject_SmallChunk_tXn60W2f8h3jgAYdEmy5NQ {
  tyObject_BaseChunk_Sdq7WpT6qAH858F5ZEdG3w Sup;
tyObject_SmallChunk_tXn60W2f8h3jgAYdEmy5NQ* next;
tyObject_SmallChunk_tXn60W2f8h3jgAYdEmy5NQ* prev;
tyObject_FreeCell_u6M5LHprqzkn9axr04yg9bGQ* freeList;
NI free;
NI acc;
NF data;
};
struct tyObject_BigChunk_Rv9c70Uhp2TytkX7eH78qEg {
  tyObject_BaseChunk_Sdq7WpT6qAH858F5ZEdG3w Sup;
tyObject_BigChunk_Rv9c70Uhp2TytkX7eH78qEg* next;
tyObject_BigChunk_Rv9c70Uhp2TytkX7eH78qEg* prev;
NF data;
};
struct tyObject_LLChunk_XsENErzHIZV9bhvyJx56wGw {
NI size;
NI acc;
tyObject_LLChunk_XsENErzHIZV9bhvyJx56wGw* next;
};
typedef NI tyArray_9a8QARi5WsUggNU9bom7kzTQ[8];
struct tyObject_Trunk_W0r8S0Y3UGke6T9bIUWnnuw {
tyObject_Trunk_W0r8S0Y3UGke6T9bIUWnnuw* next;
NI key;
tyArray_9a8QARi5WsUggNU9bom7kzTQ bits;
};
struct tyObject_PageDesc_fublkgIY4LG3mT51LU2WHg {
tyObject_PageDesc_fublkgIY4LG3mT51LU2WHg* next;
NI key;
tyArray_9a8QARi5WsUggNU9bom7kzTQ bits;
};
struct tyObject_FreeCell_u6M5LHprqzkn9axr04yg9bGQ {
tyObject_FreeCell_u6M5LHprqzkn9axr04yg9bGQ* next;
NI zeroField;
};
struct tySequence_uB9b75OUPRENsBAu4AnoePA {
  TGenericSeq Sup;
  tyObject_StackTraceEntry_oLyohQ7O2XOvGnflOss8EA data[SEQ_DECL_SIZE];
};
N_LIB_PRIVATE N_NIMCALL(void, reverse_LoixoqZetR6FfezoPedx8w)(NimStringDesc** a, NI aLen_0);
N_LIB_PRIVATE N_NIMCALL(void, reverse_XQiN4wExsmIg8NFBmG3ObA)(NimStringDesc** a, NI aLen_0, NI first, NI last);
N_LIB_PRIVATE N_NIMCALL(void, X5BX5Deq__S9coE9cSZKnhx2dOL8sov4fQ)(NimStringDesc** s, tyObject_HSlice_x7qpDivRIi6zcMSMsudNPA x, NimStringDesc* b);
static N_INLINE(NimStringDesc*, X5BX5D__xiaaX9b4cczHG39bivOynT9bgstrutils)(NimStringDesc* s, tyObject_HSlice_x7qpDivRIi6zcMSMsudNPA x);
static N_INLINE(NI, subInt)(NI a, NI b);
N_NOINLINE(void, raiseOverflow)(void);
static N_INLINE(NI, addInt)(NI a, NI b);
N_NIMCALL(NimStringDesc*, mnewString)(NI len);
N_NIMCALL(NimStringDesc*, mnewString)(NI len);
static N_INLINE(NI, chckRange)(NI i, NI a, NI b);
N_NOINLINE(void, raiseRangeError)(NI64 val);
N_NOINLINE(void, raiseIndexError)(void);
static N_INLINE(void, nimFrame)(TFrame* s);
N_LIB_PRIVATE N_NOINLINE(void, stackOverflow_II46IjNZztN9bmbxUD8dt8g)(void);
static N_INLINE(void, popFrame)(void);
static N_INLINE(NimStringDesc*, X5BX5D__lkBUIkH7j2jb0vaXPf2frAstrutils)(NimStringDesc* s, tyObject_HSlice_x7qpDivRIi6zcMSMsudNPA x);
static N_INLINE(NIM_BOOL, contains_I9cy9aN2znlBRynMcXN4pBGgstrutils)(NIM_CHAR* a, NI aLen_0, NIM_CHAR item);
static N_INLINE(NI, find_b3HPX1XboPhUmnxkTjazFQstrutils)(NIM_CHAR* a, NI aLen_0, NIM_CHAR item);
static N_INLINE(NIM_BOOL, contains_MCIiD5bOOJHgEOw1G9anbFQstrutils)(tyObject_HSlice_lKy9cDUCgy9ap43jXru18mYw s, NI value);
N_LIB_PRIVATE N_NIMCALL(NF, round_FL9bhksfuQsfLDCxRHuknsg)(NF x, NI places);
static N_INLINE(void, stareq__7kHiltrvRlcg6wSYR3CxAwstrutils)(NF* x, NF y);
static N_INLINE(void, pluseq__7kHiltrvRlcg6wSYR3CxAw_2strutils)(NF* x, NF y);
N_NIMCALL(NimStringDesc*, nimIntToStr)(NI x);
static N_INLINE(void, appendChar)(NimStringDesc* dest, NIM_CHAR c);
static N_INLINE(void, appendString)(NimStringDesc* dest, NimStringDesc* src);
static N_INLINE(void, copyMem_E1xtACub5WcDa3vbrIXbwgsystem)(void* dest, void* source, NI size);
N_NIMCALL(NimStringDesc*, rawNewString)(NI space);
N_LIB_PRIVATE N_NIMCALL(NI, npuParseInt)(NimStringDesc* s, NI* number, NI start);
N_NIMCALL(void*, newObj)(TNimType* typ, NI size);
static N_INLINE(void, asgnRefNoCycle)(void** dest, void* src);
static N_INLINE(tyObject_Cell_1zcF9cV8XIAtbN8h5HRUB8g*, usrToCell_yB9aH5WIlwd0xkYrcdPeXrQsystem)(void* usr);
static N_INLINE(void, rtlAddZCT_MV4BBk6J1qu70IbBxwEn4w_2system)(tyObject_Cell_1zcF9cV8XIAtbN8h5HRUB8g* c);
N_LIB_PRIVATE N_NOINLINE(void, addZCT_fCDI7oO1NNVXXURtxSzsRw)(tyObject_CellSeq_Axo1XVm9aaQueTOldv8le5w* s, tyObject_Cell_1zcF9cV8XIAtbN8h5HRUB8g* c);
static N_INLINE(void, asgnRef)(void** dest, void* src);
static N_INLINE(void, incRef_9cAA5YuQAAC3MVbnGeV86swsystem)(tyObject_Cell_1zcF9cV8XIAtbN8h5HRUB8g* c);
static N_INLINE(void, decRef_MV4BBk6J1qu70IbBxwEn4wsystem)(tyObject_Cell_1zcF9cV8XIAtbN8h5HRUB8g* c);
N_NIMCALL(void, raiseException)(Exception* e, NCSTRING ename);
N_LIB_PRIVATE N_NIMCALL(NIM_CHAR, nsuToLowerAsciiChar)(NIM_CHAR c);
N_LIB_PRIVATE N_NIMCALL(NI, nsuFindCharSet)(NimStringDesc* s, tySet_tyChar_nmiMWKVIe46vacnhAFrQvw chars, NI start, NI last);
N_LIB_PRIVATE N_NIMCALL(void, failedAssertImpl_aDmpBTs9cPuXp0Mp9cfiNeyA)(NimStringDesc* msg);
N_NIMCALL(NimStringDesc*, copyString)(NimStringDesc* src);
N_LIB_PRIVATE N_NIMCALL(void, nsuInitSkipTable)(NI* a, NimStringDesc* sub);
N_LIB_PRIVATE N_NIMCALL(NI, nsuFindStrA)(tyArray_9cc9aPiDa8VaWjVcFLabEDZQ a, NimStringDesc* s, NimStringDesc* sub, NI start, NI last);
N_NIMCALL(NimStringDesc*, copyStrLast)(NimStringDesc* s, NI start, NI last);
N_NIMCALL(NimStringDesc*, copyStrLast)(NimStringDesc* s, NI first, NI last);
N_NIMCALL(NimStringDesc*, resizeString)(NimStringDesc* dest, NI addlen);
N_NIMCALL(NimStringDesc*, copyStr)(NimStringDesc* s, NI start);
N_NIMCALL(NimStringDesc*, copyStr)(NimStringDesc* s, NI first);
N_NIMCALL(NimStringDesc*, rawNewString)(NI cap);
N_LIB_PRIVATE N_NIMCALL(NI, nsuFindStr)(NimStringDesc* s, NimStringDesc* sub, NI start, NI last);
N_LIB_PRIVATE N_NIMCALL(NI, nsuFindChar)(NimStringDesc* s, NIM_CHAR sub, NI start, NI last);
extern TFrame* framePtr_HRfVMH3jYeBJz6Q6X9b6Ptw;
extern TNimType NTI_yCEN9anxCD6mzBxGjuaRBdg_;
extern TNimType NTI_Gi06FkNeykJn7mrqRZYrkA_;
extern tyObject_GcHeap_1TRH1TZMaVZTnLNcIHuNFQ gch_IcYaEuuWivYAS86vFMTS3Q;
STRING_LITERAL(TM_JGc9b9bh2D3nTdUR7TGyq8aA_13, "invalid integer: ", 17);
STRING_LITERAL(TM_JGc9b9bh2D3nTdUR7TGyq8aA_20, "len(a) == L string modified while iterating over it", 51);
STRING_LITERAL(TM_JGc9b9bh2D3nTdUR7TGyq8aA_21, "", 0);

static N_INLINE(NI, subInt)(NI a, NI b) {
	NI result;
{	result = (NI)0;
	result = (NI)((NU64)(a) - (NU64)(b));
	{
		NIM_BOOL T3_;
		T3_ = (NIM_BOOL)0;
		T3_ = (((NI) 0) <= (NI)(result ^ a));
		if (T3_) goto LA4_;
		T3_ = (((NI) 0) <= (NI)(result ^ (NI)((NU64) ~(b))));
		LA4_: ;
		if (!T3_) goto LA5_;
		goto BeforeRet_;
	}
	LA5_: ;
	raiseOverflow();
	}BeforeRet_: ;
	return result;
}

static N_INLINE(NI, addInt)(NI a, NI b) {
	NI result;
{	result = (NI)0;
	result = (NI)((NU64)(a) + (NU64)(b));
	{
		NIM_BOOL T3_;
		T3_ = (NIM_BOOL)0;
		T3_ = (((NI) 0) <= (NI)(result ^ a));
		if (T3_) goto LA4_;
		T3_ = (((NI) 0) <= (NI)(result ^ b));
		LA4_: ;
		if (!T3_) goto LA5_;
		goto BeforeRet_;
	}
	LA5_: ;
	raiseOverflow();
	}BeforeRet_: ;
	return result;
}

static N_INLINE(NI, chckRange)(NI i, NI a, NI b) {
	NI result;
{	result = (NI)0;
	{
		NIM_BOOL T3_;
		T3_ = (NIM_BOOL)0;
		T3_ = (a <= i);
		if (!(T3_)) goto LA4_;
		T3_ = (i <= b);
		LA4_: ;
		if (!T3_) goto LA5_;
		result = i;
		goto BeforeRet_;
	}
	goto LA1_;
	LA5_: ;
	{
		raiseRangeError(((NI64) (i)));
	}
	LA1_: ;
	}BeforeRet_: ;
	return result;
}

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

static N_INLINE(NimStringDesc*, X5BX5D__xiaaX9b4cczHG39bivOynT9bgstrutils)(NimStringDesc* s, tyObject_HSlice_x7qpDivRIi6zcMSMsudNPA x) {
	NimStringDesc* result;
	NI a;
	NI L;
	NI TM_JGc9b9bh2D3nTdUR7TGyq8aA_2;
	NI TM_JGc9b9bh2D3nTdUR7TGyq8aA_3;
	nimfr_("[]", "system.nim");
	result = (NimStringDesc*)0;
	nimln_(3556, "system.nim");
	a = x.a;
	nimln_(3557, "system.nim");
	nimln_(3546, "system.nim");
	TM_JGc9b9bh2D3nTdUR7TGyq8aA_2 = subInt(x.b, a);
	TM_JGc9b9bh2D3nTdUR7TGyq8aA_3 = addInt((NI)(TM_JGc9b9bh2D3nTdUR7TGyq8aA_2), ((NI) 1));
	L = (NI)(TM_JGc9b9bh2D3nTdUR7TGyq8aA_3);
	nimln_(3558, "system.nim");
	result = mnewString(((NI)chckRange(L, ((NI) 0), ((NI) IL64(9223372036854775807)))));
	{
		NI i;
		NI i_2;
		i = (NI)0;
		nimln_(3519, "system.nim");
		i_2 = ((NI) 0);
		{
			nimln_(3520, "system.nim");
			while (1) {
				NI TM_JGc9b9bh2D3nTdUR7TGyq8aA_4;
				NI TM_JGc9b9bh2D3nTdUR7TGyq8aA_5;
				if (!(i_2 < L)) goto LA3;
				nimln_(3521, "system.nim");
				i = i_2;
				if ((NU)(i) > (NU)(result->Sup.len)) raiseIndexError();
				nimln_(3559, "system.nim");
				TM_JGc9b9bh2D3nTdUR7TGyq8aA_4 = addInt(i, a);
				if ((NU)((NI)(TM_JGc9b9bh2D3nTdUR7TGyq8aA_4)) > (NU)(s->Sup.len)) raiseIndexError();
				result->data[i] = s->data[(NI)(TM_JGc9b9bh2D3nTdUR7TGyq8aA_4)];
				nimln_(3522, "system.nim");
				TM_JGc9b9bh2D3nTdUR7TGyq8aA_5 = addInt(i_2, ((NI) 1));
				i_2 = (NI)(TM_JGc9b9bh2D3nTdUR7TGyq8aA_5);
			} LA3: ;
		}
	}
	popFrame();
	return result;
}

static N_INLINE(NimStringDesc*, X5BX5D__lkBUIkH7j2jb0vaXPf2frAstrutils)(NimStringDesc* s, tyObject_HSlice_x7qpDivRIi6zcMSMsudNPA x) {
	NimStringDesc* result;
	NI a;
	NI L;
	NI TM_JGc9b9bh2D3nTdUR7TGyq8aA_6;
	NI TM_JGc9b9bh2D3nTdUR7TGyq8aA_7;
	NI TM_JGc9b9bh2D3nTdUR7TGyq8aA_8;
	nimfr_("[]", "system.nim");
	result = (NimStringDesc*)0;
	nimln_(3556, "system.nim");
	a = x.a;
	nimln_(3557, "system.nim");
	nimln_(3546, "system.nim");
	nimln_(3557, "system.nim");
	TM_JGc9b9bh2D3nTdUR7TGyq8aA_6 = subInt((s ? s->Sup.len : 0), x.b);
	TM_JGc9b9bh2D3nTdUR7TGyq8aA_7 = subInt((NI)(TM_JGc9b9bh2D3nTdUR7TGyq8aA_6), a);
	TM_JGc9b9bh2D3nTdUR7TGyq8aA_8 = addInt((NI)(TM_JGc9b9bh2D3nTdUR7TGyq8aA_7), ((NI) 1));
	L = (NI)(TM_JGc9b9bh2D3nTdUR7TGyq8aA_8);
	nimln_(3558, "system.nim");
	result = mnewString(((NI)chckRange(L, ((NI) 0), ((NI) IL64(9223372036854775807)))));
	{
		NI i;
		NI i_2;
		i = (NI)0;
		nimln_(3519, "system.nim");
		i_2 = ((NI) 0);
		{
			nimln_(3520, "system.nim");
			while (1) {
				NI TM_JGc9b9bh2D3nTdUR7TGyq8aA_9;
				NI TM_JGc9b9bh2D3nTdUR7TGyq8aA_10;
				if (!(i_2 < L)) goto LA3;
				nimln_(3521, "system.nim");
				i = i_2;
				if ((NU)(i) > (NU)(result->Sup.len)) raiseIndexError();
				nimln_(3559, "system.nim");
				TM_JGc9b9bh2D3nTdUR7TGyq8aA_9 = addInt(i, a);
				if ((NU)((NI)(TM_JGc9b9bh2D3nTdUR7TGyq8aA_9)) > (NU)(s->Sup.len)) raiseIndexError();
				result->data[i] = s->data[(NI)(TM_JGc9b9bh2D3nTdUR7TGyq8aA_9)];
				nimln_(3522, "system.nim");
				TM_JGc9b9bh2D3nTdUR7TGyq8aA_10 = addInt(i_2, ((NI) 1));
				i_2 = (NI)(TM_JGc9b9bh2D3nTdUR7TGyq8aA_10);
			} LA3: ;
		}
	}
	popFrame();
	return result;
}

static N_INLINE(NI, find_b3HPX1XboPhUmnxkTjazFQstrutils)(NIM_CHAR* a, NI aLen_0, NIM_CHAR item) {
	NI result;
	nimfr_("find", "system.nim");
{	result = (NI)0;
	{
		NIM_CHAR i;
		NI i_2;
		i = (NIM_CHAR)0;
		nimln_(2185, "system.nim");
		i_2 = ((NI) 0);
		{
			nimln_(2186, "system.nim");
			while (1) {
				NI TM_JGc9b9bh2D3nTdUR7TGyq8aA_11;
				NI TM_JGc9b9bh2D3nTdUR7TGyq8aA_12;
				if (!(i_2 < aLen_0)) goto LA3;
				nimln_(2187, "system.nim");
				if ((NU)(i_2) >= (NU)(aLen_0)) raiseIndexError();
				i = a[i_2];
				nimln_(2419, "system.nim");
				{
					if (!((NU8)(i) == (NU8)(item))) goto LA6_;
					goto BeforeRet_;
				}
				LA6_: ;
				nimln_(2420, "system.nim");
				TM_JGc9b9bh2D3nTdUR7TGyq8aA_11 = addInt(result, ((NI) 1));
				result = (NI)(TM_JGc9b9bh2D3nTdUR7TGyq8aA_11);
				nimln_(2188, "system.nim");
				TM_JGc9b9bh2D3nTdUR7TGyq8aA_12 = addInt(i_2, ((NI) 1));
				i_2 = (NI)(TM_JGc9b9bh2D3nTdUR7TGyq8aA_12);
			} LA3: ;
		}
	}
	nimln_(2421, "system.nim");
	result = ((NI) -1);
	}BeforeRet_: ;
	popFrame();
	return result;
}

static N_INLINE(NIM_BOOL, contains_I9cy9aN2znlBRynMcXN4pBGgstrutils)(NIM_CHAR* a, NI aLen_0, NIM_CHAR item) {
	NIM_BOOL result;
	NI T1_;
	nimfr_("contains", "system.nim");
{	result = (NIM_BOOL)0;
	nimln_(2426, "system.nim");
	T1_ = (NI)0;
	T1_ = find_b3HPX1XboPhUmnxkTjazFQstrutils(a, aLen_0, item);
	result = (((NI) 0) <= T1_);
	goto BeforeRet_;
	}BeforeRet_: ;
	popFrame();
	return result;
}

static N_INLINE(NIM_BOOL, contains_MCIiD5bOOJHgEOw1G9anbFQstrutils)(tyObject_HSlice_lKy9cDUCgy9ap43jXru18mYw s, NI value) {
	NIM_BOOL result;
	NIM_BOOL T1_;
	nimfr_("contains", "system.nim");
	result = (NIM_BOOL)0;
	nimln_(1204, "system.nim");
	T1_ = (NIM_BOOL)0;
	T1_ = (((NI) (s.a)) <= value);
	if (!(T1_)) goto LA2_;
	T1_ = (value <= ((NI) (s.b)));
	LA2_: ;
	result = T1_;
	popFrame();
	return result;
}

static N_INLINE(void, stareq__7kHiltrvRlcg6wSYR3CxAwstrutils)(NF* x, NF y) {
	nimfr_("*=", "system.nim");
	nimln_(3710, "system.nim");
	(*x) = ((NF)((*x)) * (NF)(y));
	popFrame();
}

static N_INLINE(void, pluseq__7kHiltrvRlcg6wSYR3CxAw_2strutils)(NF* x, NF y) {
	nimfr_("+=", "system.nim");
	nimln_(3700, "system.nim");
	(*x) = ((NF)((*x)) + (NF)(y));
	popFrame();
}

static N_INLINE(void, appendChar)(NimStringDesc* dest, NIM_CHAR c) {
	(*dest).data[((*dest).Sup.len)- 0] = c;
	(*dest).data[((NI)((*dest).Sup.len + ((NI) 1)))- 0] = 0;
	(*dest).Sup.len += ((NI) 1);
}

static N_INLINE(void, copyMem_E1xtACub5WcDa3vbrIXbwgsystem)(void* dest, void* source, NI size) {
	void* T1_;
	T1_ = (void*)0;
	T1_ = memcpy(dest, source, ((size_t) (size)));
}

static N_INLINE(void, appendString)(NimStringDesc* dest, NimStringDesc* src) {
	copyMem_E1xtACub5WcDa3vbrIXbwgsystem(((void*) ((&(*dest).data[((*dest).Sup.len)- 0]))), ((void*) ((*src).data)), ((NI) ((NI)((*src).Sup.len + ((NI) 1)))));
	(*dest).Sup.len += (*src).Sup.len;
}

N_LIB_PRIVATE N_NIMCALL(NimStringDesc*, nsuIntToStr)(NI x, NI minchars) {
	NimStringDesc* result;
	nimfr_("intToStr", "strutils.nim");
	result = (NimStringDesc*)0;
	result = nimIntToStr((x > 0? (x) : -(x)));
	{
		NI i;
		NI colontmp_;
		NI res;
		i = (NI)0;
		colontmp_ = (NI)0;
		colontmp_ = (NI)(((NI) (minchars)) - (result ? result->Sup.len : 0));
		res = ((NI) 1);
		{
			while (1) {
				NimStringDesc* T4_;
				if (!(res <= colontmp_)) goto LA3;
				i = res;
				T4_ = (NimStringDesc*)0;
				T4_ = rawNewString(result->Sup.len + 1);
appendChar(T4_, 48);
appendString(T4_, result);
				result = T4_;
				res += ((NI) 1);
			} LA3: ;
		}
	}
	{
		NimStringDesc* T9_;
		if (!(x < ((NI) 0))) goto LA7_;
		T9_ = (NimStringDesc*)0;
		T9_ = rawNewString(result->Sup.len + 1);
appendChar(T9_, 45);
appendString(T9_, result);
		result = T9_;
	}
	LA7_: ;
	popFrame();
	return result;
}

N_LIB_PRIVATE N_NIMCALL(NimStringDesc*, nsuRepeatChar)(NIM_CHAR c, NI count) {
	NimStringDesc* result;
	nimfr_("repeat", "strutils.nim");
	result = (NimStringDesc*)0;
	result = mnewString(count);
	{
		NI i;
		NI colontmp_;
		NI res;
		i = (NI)0;
		colontmp_ = (NI)0;
		colontmp_ = (NI)(((NI) (count)) - ((NI) 1));
		res = ((NI) 0);
		{
			while (1) {
				if (!(res <= colontmp_)) goto LA3;
				i = res;
				result->data[i] = c;
				res += ((NI) 1);
			} LA3: ;
		}
	}
	popFrame();
	return result;
}

static N_INLINE(tyObject_Cell_1zcF9cV8XIAtbN8h5HRUB8g*, usrToCell_yB9aH5WIlwd0xkYrcdPeXrQsystem)(void* usr) {
	tyObject_Cell_1zcF9cV8XIAtbN8h5HRUB8g* result;
	nimfr_("usrToCell", "gc.nim");
	result = (tyObject_Cell_1zcF9cV8XIAtbN8h5HRUB8g*)0;
	nimln_(132, "gc.nim");
	result = ((tyObject_Cell_1zcF9cV8XIAtbN8h5HRUB8g*) ((NI)((NU64)(((NI) (ptrdiff_t) (usr))) - (NU64)(((NI)sizeof(tyObject_Cell_1zcF9cV8XIAtbN8h5HRUB8g))))));
	popFrame();
	return result;
}

static N_INLINE(void, rtlAddZCT_MV4BBk6J1qu70IbBxwEn4w_2system)(tyObject_Cell_1zcF9cV8XIAtbN8h5HRUB8g* c) {
	nimfr_("rtlAddZCT", "gc.nim");
	nimln_(211, "gc.nim");
	addZCT_fCDI7oO1NNVXXURtxSzsRw((&gch_IcYaEuuWivYAS86vFMTS3Q.zct), c);
	popFrame();
}

static N_INLINE(void, asgnRefNoCycle)(void** dest, void* src) {
	nimfr_("asgnRefNoCycle", "gc.nim");
	nimln_(271, "gc.nim");
	{
		tyObject_Cell_1zcF9cV8XIAtbN8h5HRUB8g* c;
		nimln_(398, "system.nim");
		nimln_(271, "gc.nim");
		if (!!((src == NIM_NIL))) goto LA3_;
		nimln_(272, "gc.nim");
		c = usrToCell_yB9aH5WIlwd0xkYrcdPeXrQsystem(src);
		nimln_(273, "gc.nim");
		(*c).refcount += ((NI) 8);
	}
	LA3_: ;
	nimln_(274, "gc.nim");
	{
		tyObject_Cell_1zcF9cV8XIAtbN8h5HRUB8g* c_2;
		nimln_(398, "system.nim");
		nimln_(274, "gc.nim");
		if (!!(((*dest) == NIM_NIL))) goto LA7_;
		nimln_(275, "gc.nim");
		c_2 = usrToCell_yB9aH5WIlwd0xkYrcdPeXrQsystem((*dest));
		nimln_(276, "gc.nim");
		{
			(*c_2).refcount -= ((NI) 8);
			if (!((NU64)((*c_2).refcount) < (NU64)(((NI) 8)))) goto LA11_;
			nimln_(277, "gc.nim");
			rtlAddZCT_MV4BBk6J1qu70IbBxwEn4w_2system(c_2);
		}
		LA11_: ;
	}
	LA7_: ;
	nimln_(278, "gc.nim");
	(*dest) = src;
	popFrame();
}

static N_INLINE(void, incRef_9cAA5YuQAAC3MVbnGeV86swsystem)(tyObject_Cell_1zcF9cV8XIAtbN8h5HRUB8g* c) {
	nimfr_("incRef", "gc.nim");
	nimln_(191, "gc.nim");
	(*c).refcount = (NI)((NU64)((*c).refcount) + (NU64)(((NI) 8)));
	popFrame();
}

static N_INLINE(void, decRef_MV4BBk6J1qu70IbBxwEn4wsystem)(tyObject_Cell_1zcF9cV8XIAtbN8h5HRUB8g* c) {
	nimfr_("decRef", "gc.nim");
	nimln_(218, "gc.nim");
	{
		(*c).refcount -= ((NI) 8);
		if (!((NU64)((*c).refcount) < (NU64)(((NI) 8)))) goto LA3_;
		nimln_(219, "gc.nim");
		rtlAddZCT_MV4BBk6J1qu70IbBxwEn4w_2system(c);
	}
	LA3_: ;
	popFrame();
}

static N_INLINE(void, asgnRef)(void** dest, void* src) {
	nimfr_("asgnRef", "gc.nim");
	nimln_(264, "gc.nim");
	{
		tyObject_Cell_1zcF9cV8XIAtbN8h5HRUB8g* T5_;
		nimln_(398, "system.nim");
		nimln_(264, "gc.nim");
		if (!!((src == NIM_NIL))) goto LA3_;
		T5_ = (tyObject_Cell_1zcF9cV8XIAtbN8h5HRUB8g*)0;
		T5_ = usrToCell_yB9aH5WIlwd0xkYrcdPeXrQsystem(src);
		incRef_9cAA5YuQAAC3MVbnGeV86swsystem(T5_);
	}
	LA3_: ;
	nimln_(265, "gc.nim");
	{
		tyObject_Cell_1zcF9cV8XIAtbN8h5HRUB8g* T10_;
		nimln_(398, "system.nim");
		nimln_(265, "gc.nim");
		if (!!(((*dest) == NIM_NIL))) goto LA8_;
		T10_ = (tyObject_Cell_1zcF9cV8XIAtbN8h5HRUB8g*)0;
		T10_ = usrToCell_yB9aH5WIlwd0xkYrcdPeXrQsystem((*dest));
		decRef_MV4BBk6J1qu70IbBxwEn4wsystem(T10_);
	}
	LA8_: ;
	nimln_(266, "gc.nim");
	(*dest) = src;
	popFrame();
}

N_LIB_PRIVATE N_NIMCALL(NI, nsuParseInt)(NimStringDesc* s) {
	NI result;
	NI L;
	nimfr_("parseInt", "strutils.nim");
	result = (NI)0;
	L = npuParseInt(s, (&result), ((NI) 0));
	{
		NIM_BOOL T3_;
		tyObject_ValueError_Gi06FkNeykJn7mrqRZYrkA* e;
		NimStringDesc* T7_;
		T3_ = (NIM_BOOL)0;
		T3_ = !((L == (s ? s->Sup.len : 0)));
		if (T3_) goto LA4_;
		T3_ = (L == ((NI) 0));
		LA4_: ;
		if (!T3_) goto LA5_;
		e = (tyObject_ValueError_Gi06FkNeykJn7mrqRZYrkA*)0;
		e = (tyObject_ValueError_Gi06FkNeykJn7mrqRZYrkA*) newObj((&NTI_yCEN9anxCD6mzBxGjuaRBdg_), sizeof(tyObject_ValueError_Gi06FkNeykJn7mrqRZYrkA));
		(*e).Sup.Sup.m_type = (&NTI_Gi06FkNeykJn7mrqRZYrkA_);
		T7_ = (NimStringDesc*)0;
		T7_ = rawNewString(s->Sup.len + 17);
appendString(T7_, ((NimStringDesc*) &TM_JGc9b9bh2D3nTdUR7TGyq8aA_13));
appendString(T7_, s);
		asgnRefNoCycle((void**) (&(*e).Sup.message), T7_);
		asgnRef((void**) (&(*e).Sup.parent), NIM_NIL);
		raiseException((Exception*)e, "ValueError");
	}
	LA5_: ;
	popFrame();
	return result;
}

N_LIB_PRIVATE N_NIMCALL(NIM_CHAR, nsuToLowerAsciiChar)(NIM_CHAR c) {
	NIM_CHAR result;
	nimfr_("toLowerAscii", "strutils.nim");
	result = (NIM_CHAR)0;
	nimln_(207, "strutils.nim");
	{
		NI TM_JGc9b9bh2D3nTdUR7TGyq8aA_15;
		if (!(((NU8)(c)) >= ((NU8)(65)) && ((NU8)(c)) <= ((NU8)(90)))) goto LA3_;
		nimln_(208, "strutils.nim");
		TM_JGc9b9bh2D3nTdUR7TGyq8aA_15 = addInt(((NU8)(c)), ((NI) 32));
		result = ((NIM_CHAR) (((NI)chckRange((NI)(TM_JGc9b9bh2D3nTdUR7TGyq8aA_15), ((NI) 0), ((NI) 255)))));
	}
	goto LA1_;
	LA3_: ;
	{
		nimln_(210, "strutils.nim");
		result = c;
	}
	LA1_: ;
	popFrame();
	return result;
}

N_LIB_PRIVATE N_NIMCALL(NimStringDesc*, nsuToLowerAsciiStr)(NimStringDesc* s) {
	NimStringDesc* result;
	nimfr_("toLowerAscii", "strutils.nim");
	result = (NimStringDesc*)0;
	nimln_(219, "strutils.nim");
	result = mnewString(((NI)chckRange((s ? s->Sup.len : 0), ((NI) 0), ((NI) IL64(9223372036854775807)))));
	{
		NI i;
		NI colontmp_;
		NI TM_JGc9b9bh2D3nTdUR7TGyq8aA_14;
		NI res;
		i = (NI)0;
		colontmp_ = (NI)0;
		nimln_(220, "strutils.nim");
		TM_JGc9b9bh2D3nTdUR7TGyq8aA_14 = subInt((s ? s->Sup.len : 0), ((NI) 1));
		colontmp_ = (NI)(TM_JGc9b9bh2D3nTdUR7TGyq8aA_14);
		nimln_(2045, "system.nim");
		res = ((NI) 0);
		{
			nimln_(2046, "system.nim");
			while (1) {
				NI TM_JGc9b9bh2D3nTdUR7TGyq8aA_16;
				if (!(res <= colontmp_)) goto LA3;
				nimln_(2047, "system.nim");
				i = res;
				if ((NU)(i) > (NU)(result->Sup.len)) raiseIndexError();
				nimln_(221, "strutils.nim");
				if ((NU)(i) > (NU)(s->Sup.len)) raiseIndexError();
				result->data[i] = nsuToLowerAsciiChar(s->data[i]);
				nimln_(2048, "system.nim");
				TM_JGc9b9bh2D3nTdUR7TGyq8aA_16 = addInt(res, ((NI) 1));
				res = (NI)(TM_JGc9b9bh2D3nTdUR7TGyq8aA_16);
			} LA3: ;
		}
	}
	popFrame();
	return result;
}

N_LIB_PRIVATE N_NIMCALL(NI, nsuCmpIgnoreCase)(NimStringDesc* a, NimStringDesc* b) {
	NI result;
	NI i;
	NI m;
	NI TM_JGc9b9bh2D3nTdUR7TGyq8aA_19;
	nimfr_("cmpIgnoreCase", "strutils.nim");
{	result = (NI)0;
	nimln_(408, "strutils.nim");
	i = ((NI) 0);
	nimln_(409, "strutils.nim");
	m = (((a ? a->Sup.len : 0) <= (b ? b->Sup.len : 0)) ? (a ? a->Sup.len : 0) : (b ? b->Sup.len : 0));
	{
		nimln_(410, "strutils.nim");
		while (1) {
			NIM_CHAR T3_;
			NIM_CHAR T4_;
			NI TM_JGc9b9bh2D3nTdUR7TGyq8aA_17;
			NI TM_JGc9b9bh2D3nTdUR7TGyq8aA_18;
			if (!(i < m)) goto LA2;
			nimln_(411, "strutils.nim");
			if ((NU)(i) > (NU)(a->Sup.len)) raiseIndexError();
			T3_ = (NIM_CHAR)0;
			T3_ = nsuToLowerAsciiChar(a->data[i]);
			if ((NU)(i) > (NU)(b->Sup.len)) raiseIndexError();
			T4_ = (NIM_CHAR)0;
			T4_ = nsuToLowerAsciiChar(b->data[i]);
			TM_JGc9b9bh2D3nTdUR7TGyq8aA_17 = subInt(((NU8)(T3_)), ((NU8)(T4_)));
			result = (NI)(TM_JGc9b9bh2D3nTdUR7TGyq8aA_17);
			nimln_(412, "strutils.nim");
			{
				nimln_(398, "system.nim");
				nimln_(412, "strutils.nim");
				if (!!((result == ((NI) 0)))) goto LA7_;
				goto BeforeRet_;
			}
			LA7_: ;
			nimln_(413, "strutils.nim");
			TM_JGc9b9bh2D3nTdUR7TGyq8aA_18 = addInt(i, ((NI) 1));
			i = (NI)(TM_JGc9b9bh2D3nTdUR7TGyq8aA_18);
		} LA2: ;
	}
	nimln_(414, "strutils.nim");
	TM_JGc9b9bh2D3nTdUR7TGyq8aA_19 = subInt((a ? a->Sup.len : 0), (b ? b->Sup.len : 0));
	result = (NI)(TM_JGc9b9bh2D3nTdUR7TGyq8aA_19);
	}BeforeRet_: ;
	popFrame();
	return result;
}

N_LIB_PRIVATE N_NIMCALL(NIM_BOOL, nsuStartsWith)(NimStringDesc* s, NimStringDesc* prefix) {
	NIM_BOOL result;
	NI i;
	nimfr_("startsWith", "strutils.nim");
{	result = (NIM_BOOL)0;
	i = ((NI) 0);
	{
		while (1) {
			{
				if (!((NU8)(prefix->data[i]) == (NU8)(0))) goto LA5_;
				result = NIM_TRUE;
				goto BeforeRet_;
			}
			LA5_: ;
			{
				if (!!(((NU8)(s->data[i]) == (NU8)(prefix->data[i])))) goto LA9_;
				result = NIM_FALSE;
				goto BeforeRet_;
			}
			LA9_: ;
			i += ((NI) 1);
		}
	}
	}BeforeRet_: ;
	popFrame();
	return result;
}

N_LIB_PRIVATE N_NIMCALL(NI, nsuFindChar)(NimStringDesc* s, NIM_CHAR sub, NI start, NI last) {
	NI result;
	NI last_2;
	void* found;
	nimfr_("find", "strutils.nim");
{	result = (NI)0;
	{
		if (!(((NI) (last)) == ((NI) 0))) goto LA3_;
		last_2 = (s ? (s->Sup.len-1) : -1);
	}
	goto LA1_;
	LA3_: ;
	{
		last_2 = ((NI) (last));
	}
	LA1_: ;
	found = memchr(((void*) ((&s->data[start]))), sub, (NI)((NI)(last_2 - ((NI) (start))) + ((NI) 1)));
	{
		if (!!((found == 0))) goto LA8_;
		result = (NI)((NU64)(((NI) (ptrdiff_t) (found))) - (NU64)(((NI) (s->data))));
		goto BeforeRet_;
	}
	LA8_: ;
	result = ((NI) -1);
	goto BeforeRet_;
	}BeforeRet_: ;
	popFrame();
	return result;
}

N_LIB_PRIVATE N_NIMCALL(NI, nsuFindCharSet)(NimStringDesc* s, tySet_tyChar_nmiMWKVIe46vacnhAFrQvw chars, NI start, NI last) {
	NI result;
	NI last_2;
	nimfr_("find", "strutils.nim");
{	result = (NI)0;
	{
		if (!(((NI) (last)) == ((NI) 0))) goto LA3_;
		last_2 = (s ? (s->Sup.len-1) : -1);
	}
	goto LA1_;
	LA3_: ;
	{
		last_2 = ((NI) (last));
	}
	LA1_: ;
	{
		NI i;
		NI colontmp_;
		NI res;
		i = (NI)0;
		colontmp_ = (NI)0;
		colontmp_ = ((NI) (last_2));
		res = ((NI) (start));
		{
			while (1) {
				if (!(res <= ((NI) (colontmp_)))) goto LA8;
				i = ((NI) (res));
				{
					if (!((chars[(NU)(((NU8)(s->data[i])))>>3] &(1U<<((NU)(((NU8)(s->data[i])))&7U)))!=0)) goto LA11_;
					result = ((NI) (i));
					goto BeforeRet_;
				}
				LA11_: ;
				res += ((NI) 1);
			} LA8: ;
		}
	}
	result = ((NI) -1);
	goto BeforeRet_;
	}BeforeRet_: ;
	popFrame();
	return result;
}

N_LIB_PRIVATE N_NIMCALL(NIM_BOOL, contains_m1TSS3QwQPclQATuiRuVZg)(NimStringDesc* s, tySet_tyChar_nmiMWKVIe46vacnhAFrQvw chars) {
	NIM_BOOL result;
	NI T1_;
	nimfr_("contains", "strutils.nim");
{	result = (NIM_BOOL)0;
	T1_ = (NI)0;
	T1_ = nsuFindCharSet(s, chars, ((NI) 0), ((NI) 0));
	result = (((NI) 0) <= T1_);
	goto BeforeRet_;
	}BeforeRet_: ;
	popFrame();
	return result;
}

N_LIB_PRIVATE N_NIMCALL(NIM_BOOL, allCharsInSet_wVfr4F6j4mVzI8ggLoMVdw)(NimStringDesc* s, tySet_tyChar_nmiMWKVIe46vacnhAFrQvw theSet) {
	NIM_BOOL result;
	nimfr_("allCharsInSet", "strutils.nim");
{	result = (NIM_BOOL)0;
	{
		NIM_CHAR c;
		NI i;
		NI L;
		c = (NIM_CHAR)0;
		i = ((NI) 0);
		L = (s ? s->Sup.len : 0);
		{
			while (1) {
				if (!(i < L)) goto LA3;
				c = s->data[i];
				{
					if (!!(((theSet[(NU)(((NU8)(c)))>>3] &(1U<<((NU)(((NU8)(c)))&7U)))!=0))) goto LA6_;
					result = NIM_FALSE;
					goto BeforeRet_;
				}
				LA6_: ;
				i += ((NI) 1);
				{
					if (!!(((s ? s->Sup.len : 0) == L))) goto LA10_;
					failedAssertImpl_aDmpBTs9cPuXp0Mp9cfiNeyA(((NimStringDesc*) &TM_JGc9b9bh2D3nTdUR7TGyq8aA_20));
				}
				LA10_: ;
			} LA3: ;
		}
	}
	result = NIM_TRUE;
	goto BeforeRet_;
	}BeforeRet_: ;
	popFrame();
	return result;
}

N_LIB_PRIVATE N_NIMCALL(void, nsuInitSkipTable)(NI* a, NimStringDesc* sub) {
	NI m;
	NI m1;
	NI i;
	nimfr_("initSkipTable", "strutils.nim");
	m = (sub ? sub->Sup.len : 0);
	m1 = (NI)(m + ((NI) 1));
	i = ((NI) 0);
	{
		while (1) {
			if (!(i <= ((NI) 248))) goto LA2;
			a[(((NU8)(((NIM_CHAR) (((NI) ((NI)(i + ((NI) 0)))))))))- 0] = m1;
			a[(((NU8)(((NIM_CHAR) (((NI) ((NI)(i + ((NI) 1)))))))))- 0] = m1;
			a[(((NU8)(((NIM_CHAR) (((NI) ((NI)(i + ((NI) 2)))))))))- 0] = m1;
			a[(((NU8)(((NIM_CHAR) (((NI) ((NI)(i + ((NI) 3)))))))))- 0] = m1;
			a[(((NU8)(((NIM_CHAR) (((NI) ((NI)(i + ((NI) 4)))))))))- 0] = m1;
			a[(((NU8)(((NIM_CHAR) (((NI) ((NI)(i + ((NI) 5)))))))))- 0] = m1;
			a[(((NU8)(((NIM_CHAR) (((NI) ((NI)(i + ((NI) 6)))))))))- 0] = m1;
			a[(((NU8)(((NIM_CHAR) (((NI) ((NI)(i + ((NI) 7)))))))))- 0] = m1;
			i += ((NI) 8);
		} LA2: ;
	}
	{
		NI i_2;
		NI colontmp_;
		NI res;
		i_2 = (NI)0;
		colontmp_ = (NI)0;
		colontmp_ = (NI)(m - ((NI) 1));
		res = ((NI) 0);
		{
			while (1) {
				if (!(res <= colontmp_)) goto LA5;
				i_2 = res;
				a[(((NU8)(sub->data[i_2])))- 0] = (NI)(m - i_2);
				res += ((NI) 1);
			} LA5: ;
		}
	}
	popFrame();
}

N_LIB_PRIVATE N_NIMCALL(NI, nsuFindStrA)(tyArray_9cc9aPiDa8VaWjVcFLabEDZQ a, NimStringDesc* s, NimStringDesc* sub, NI start, NI last) {
	NI result;
	NI last_2;
	NI m;
	NI n;
	NI j;
	nimfr_("find", "strutils.nim");
{	result = (NI)0;
	{
		if (!(((NI) (last)) == ((NI) 0))) goto LA3_;
		last_2 = (s ? (s->Sup.len-1) : -1);
	}
	goto LA1_;
	LA3_: ;
	{
		last_2 = ((NI) (last));
	}
	LA1_: ;
	m = (sub ? sub->Sup.len : 0);
	n = (NI)(last_2 + ((NI) 1));
	j = start;
	{
		while (1) {
			if (!(((NI) (j)) <= (NI)(n - m))) goto LA7;
			{
				{
					NI k;
					NI colontmp_;
					NI res;
					k = (NI)0;
					colontmp_ = (NI)0;
					colontmp_ = (NI)(m - ((NI) 1));
					res = ((NI) 0);
					{
						while (1) {
							if (!(res <= colontmp_)) goto LA11;
							k = res;
							{
								if (!!(((NU8)(sub->data[k]) == (NU8)(s->data[(NI)(k + ((NI) (j)))])))) goto LA14_;
								goto LA8;
							}
							LA14_: ;
							res += ((NI) 1);
						} LA11: ;
					}
				}
				result = ((NI) (j));
				goto BeforeRet_;
			} LA8: ;
			j += a[(((NU8)(s->data[(NI)(((NI) (j)) + m)])))- 0];
		} LA7: ;
	}
	result = ((NI) -1);
	goto BeforeRet_;
	}BeforeRet_: ;
	popFrame();
	return result;
}

N_LIB_PRIVATE N_NIMCALL(NimStringDesc*, nsuReplaceStr)(NimStringDesc* s, NimStringDesc* sub, NimStringDesc* by) {
	NimStringDesc* result;
	tyArray_9cc9aPiDa8VaWjVcFLabEDZQ a;
	NI last;
	NI i;
	NimStringDesc* T8_;
	nimfr_("replace", "strutils.nim");
	result = (NimStringDesc*)0;
	result = copyString(((NimStringDesc*) &TM_JGc9b9bh2D3nTdUR7TGyq8aA_21));
	nsuInitSkipTable(a, sub);
	last = (s ? (s->Sup.len-1) : -1);
	i = ((NI) 0);
	{
		while (1) {
			NI j;
			NimStringDesc* T7_;
			j = nsuFindStrA(a, s, sub, ((NI) (i)), ((NI) (last)));
			{
				if (!(j < ((NI) 0))) goto LA5_;
				goto LA1;
			}
			LA5_: ;
			T7_ = (NimStringDesc*)0;
			T7_ = copyStrLast(s, i, (NI)(j - ((NI) 1)));
			result = resizeString(result, T7_->Sup.len + 0);
appendString(result, T7_);
			result = resizeString(result, by->Sup.len + 0);
appendString(result, by);
			i = (NI)(j + (sub ? sub->Sup.len : 0));
		}
	} LA1: ;
	T8_ = (NimStringDesc*)0;
	T8_ = copyStr(s, i);
	result = resizeString(result, T8_->Sup.len + 0);
appendString(result, T8_);
	popFrame();
	return result;
}

N_LIB_PRIVATE N_NIMCALL(NI, nsuCmpIgnoreStyle)(NimStringDesc* a, NimStringDesc* b) {
	NI result;
	NI i;
	NI j;
	nimfr_("cmpIgnoreStyle", "strutils.nim");
	result = (NI)0;
	i = ((NI) 0);
	j = ((NI) 0);
	{
		while (1) {
			NIM_CHAR aa;
			NIM_CHAR bb;
			{
				while (1) {
					if (!((NU8)(a->data[i]) == (NU8)(95))) goto LA4;
					i += ((NI) 1);
				} LA4: ;
			}
			{
				while (1) {
					if (!((NU8)(b->data[j]) == (NU8)(95))) goto LA6;
					j += ((NI) 1);
				} LA6: ;
			}
			aa = nsuToLowerAsciiChar(a->data[i]);
			bb = nsuToLowerAsciiChar(b->data[j]);
			result = (NI)(((NU8)(aa)) - ((NU8)(bb)));
			{
				NIM_BOOL T9_;
				T9_ = (NIM_BOOL)0;
				T9_ = !((result == ((NI) 0)));
				if (T9_) goto LA10_;
				T9_ = ((NU8)(aa) == (NU8)(0));
				LA10_: ;
				if (!T9_) goto LA11_;
				goto LA1;
			}
			LA11_: ;
			i += ((NI) 1);
			j += ((NI) 1);
		}
	} LA1: ;
	popFrame();
	return result;
}

N_LIB_PRIVATE N_NIMCALL(NimStringDesc*, nsuJoinSep)(NimStringDesc** a, NI aLen_0, NimStringDesc* sep) {
	NimStringDesc* result;
	nimfr_("join", "strutils.nim");
	result = (NimStringDesc*)0;
	{
		NI L;
		if (!(((NI) 0) < aLen_0)) goto LA3_;
		L = (NI)((sep ? sep->Sup.len : 0) * (NI)(aLen_0 - ((NI) 1)));
		{
			NI i;
			NI colontmp_;
			NI res;
			i = (NI)0;
			colontmp_ = (NI)0;
			colontmp_ = (aLen_0-1);
			res = ((NI) 0);
			{
				while (1) {
					if (!(res <= colontmp_)) goto LA7;
					i = res;
					L += (a[i] ? a[i]->Sup.len : 0);
					res += ((NI) 1);
				} LA7: ;
			}
		}
		result = rawNewString(((NI) (L)));
		result = resizeString(result, a[((NI) 0)]->Sup.len + 0);
appendString(result, a[((NI) 0)]);
		{
			NI i_2;
			NI colontmp__2;
			NI res_2;
			i_2 = (NI)0;
			colontmp__2 = (NI)0;
			colontmp__2 = (aLen_0-1);
			res_2 = ((NI) 1);
			{
				while (1) {
					if (!(res_2 <= colontmp__2)) goto LA10;
					i_2 = res_2;
					result = resizeString(result, sep->Sup.len + 0);
appendString(result, sep);
					result = resizeString(result, a[i_2]->Sup.len + 0);
appendString(result, a[i_2]);
					res_2 += ((NI) 1);
				} LA10: ;
			}
		}
	}
	goto LA1_;
	LA3_: ;
	{
		result = copyString(((NimStringDesc*) &TM_JGc9b9bh2D3nTdUR7TGyq8aA_21));
	}
	LA1_: ;
	popFrame();
	return result;
}

N_LIB_PRIVATE N_NIMCALL(NI, nsuFindStr)(NimStringDesc* s, NimStringDesc* sub, NI start, NI last) {
	NI result;
	tyArray_9cc9aPiDa8VaWjVcFLabEDZQ a;
	nimfr_("find", "strutils.nim");
{	result = (NI)0;
	{
		if (!((s ? s->Sup.len : 0) < (sub ? sub->Sup.len : 0))) goto LA3_;
		result = ((NI) -1);
		goto BeforeRet_;
	}
	LA3_: ;
	{
		if (!((sub ? sub->Sup.len : 0) == ((NI) 1))) goto LA7_;
		result = nsuFindChar(s, sub->data[((NI) 0)], start, last);
		goto BeforeRet_;
	}
	LA7_: ;
	nsuInitSkipTable(a, sub);
	result = nsuFindStrA(a, s, sub, start, last);
	}BeforeRet_: ;
	popFrame();
	return result;
}

N_LIB_PRIVATE N_NIMCALL(NIM_BOOL, contains_bKoQGynT9bWCEn79aXG8be9aw)(NimStringDesc* s, NimStringDesc* sub) {
	NIM_BOOL result;
	NI T1_;
	nimfr_("contains", "strutils.nim");
{	result = (NIM_BOOL)0;
	T1_ = (NI)0;
	T1_ = nsuFindStr(s, sub, ((NI) 0), ((NI) 0));
	result = (((NI) 0) <= T1_);
	goto BeforeRet_;
	}BeforeRet_: ;
	popFrame();
	return result;
}
NIM_EXTERNC N_NOINLINE(void, stdlib_strutilsInit000)(void) {
	nimfr_("strutils", "strutils.nim");
	popFrame();
}

NIM_EXTERNC N_NOINLINE(void, stdlib_strutilsDatInit000)(void) {
}

