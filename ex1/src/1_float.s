	.text
	.cstring
lC2:
	.ascii "ff: %.32f\12df: %.32f\12\0"
	.text
	.p2align 4
	.globl _float_double
_float_double:
LFB1:
	movsd	lC0(%rip), %xmm1
	leaq	lC2(%rip), %rdi
	movl	$2, %eax
	movsd	lC1(%rip), %xmm0
	jmp	_printf
LFE1:
	.p2align 4
	.globl _a1_add_100a3_way1
_a1_add_100a3_way1:
LFB2:
	movl	$100, %eax
	.p2align 4,,10
	.p2align 3
L4:
	subl	$1, %eax
	addss	%xmm1, %xmm0
	jne	L4
	ret
LFE2:
	.p2align 4
	.globl _a1_add_100a3_way2
_a1_add_100a3_way2:
LFB3:
	movl	$100, %eax
	movaps	%xmm0, %xmm2
	pxor	%xmm0, %xmm0
	.p2align 4,,10
	.p2align 3
L7:
	subl	$1, %eax
	addss	%xmm1, %xmm0
	jne	L7
	addss	%xmm2, %xmm0
	ret
LFE3:
	.cstring
	.align 3
lC5:
	.ascii "1) \344\270\244\347\247\215\347\256\227\346\263\225\350\256\241\347\256\227a1\344\270\216"
	.ascii "100\344\270\252a3\347\233\270\345\212\240\347\232\204\347\273\223\346\236\234\0"
	.align 3
lC7:
	.ascii "\346\226\271\346\263\225"
	.ascii "1: %.32f\12\346\226\271\346\263\225"
	.ascii "2: %.32f\12\0"
lC8:
	.ascii "2) \350\256\241\347\256\227 a1/a3+a2\0"
lC10:
	.ascii "result: %.32f\12\0"
lC11:
	.ascii "\350\256\241\347\256\227a1-a2\0"
	.text
	.p2align 4
	.globl _float_calc
_float_calc:
LFB4:
	leaq	lC5(%rip), %rdi
	subq	$8, %rsp
LCFI0:
	call	_puts
	movss	lC4(%rip), %xmm3
	movl	$100, %eax
	movss	lC6(%rip), %xmm2
	movaps	%xmm3, %xmm0
	.p2align 4,,10
	.p2align 3
L10:
	subl	$1, %eax
	addss	%xmm2, %xmm0
	jne	L10
	movl	$100, %eax
	pxor	%xmm1, %xmm1
	.p2align 4,,10
	.p2align 3
L11:
	subl	$1, %eax
	addss	%xmm2, %xmm1
	jne	L11
	addss	%xmm3, %xmm1
	leaq	lC7(%rip), %rdi
	movl	$2, %eax
	cvtss2sd	%xmm0, %xmm0
	cvtss2sd	%xmm1, %xmm1
	call	_printf
	leaq	lC8(%rip), %rdi
	call	_puts
	movsd	lC9(%rip), %xmm0
	movl	$1, %eax
	leaq	lC10(%rip), %rdi
	call	_printf
	leaq	lC11(%rip), %rdi
	call	_puts
	movsd	lC12(%rip), %xmm0
	movl	$1, %eax
	addq	$8, %rsp
LCFI1:
	leaq	lC10(%rip), %rdi
	jmp	_printf
LFE4:
	.cstring
lC13:
	.ascii "\12"
	.ascii "1.(1)\0"
lC14:
	.ascii "\12"
	.ascii "1.(2)\0"
	.section __TEXT,__text_startup,regular,pure_instructions
	.p2align 4
	.globl _main
_main:
LFB5:
	leaq	lC13(%rip), %rdi
	subq	$8, %rsp
LCFI2:
	call	_puts
	movsd	lC0(%rip), %xmm1
	movl	$2, %eax
	movsd	lC1(%rip), %xmm0
	leaq	lC2(%rip), %rdi
	call	_printf
	leaq	lC14(%rip), %rdi
	call	_puts
	xorl	%eax, %eax
	call	_float_calc
	xorl	%eax, %eax
	addq	$8, %rsp
LCFI3:
	ret
LFE5:
	.literal8
	.align 3
lC0:
	.long	927397471
	.long	1069521629
	.align 3
lC1:
	.long	1073741824
	.long	1069521629
	.literal4
	.align 2
lC4:
	.long	1065353224
	.align 2
lC6:
	.long	869711765
	.literal8
	.align 3
lC9:
	.long	1073741824
	.long	1097011921
	.align 3
lC12:
	.long	0
	.long	1051721728
	.section __TEXT,__eh_frame,coalesced,no_toc+strip_static_syms+live_support
EH_frame1:
	.set L$set$0,LECIE1-LSCIE1
	.long L$set$0
LSCIE1:
	.long	0
	.byte	0x1
	.ascii "zR\0"
	.byte	0x1
	.byte	0x78
	.byte	0x10
	.byte	0x1
	.byte	0x10
	.byte	0xc
	.byte	0x7
	.byte	0x8
	.byte	0x90
	.byte	0x1
	.align 3
LECIE1:
LSFDE1:
	.set L$set$1,LEFDE1-LASFDE1
	.long L$set$1
LASFDE1:
	.long	LASFDE1-EH_frame1
	.quad	LFB1-.
	.set L$set$2,LFE1-LFB1
	.quad L$set$2
	.byte	0
	.align 3
LEFDE1:
LSFDE3:
	.set L$set$3,LEFDE3-LASFDE3
	.long L$set$3
LASFDE3:
	.long	LASFDE3-EH_frame1
	.quad	LFB2-.
	.set L$set$4,LFE2-LFB2
	.quad L$set$4
	.byte	0
	.align 3
LEFDE3:
LSFDE5:
	.set L$set$5,LEFDE5-LASFDE5
	.long L$set$5
LASFDE5:
	.long	LASFDE5-EH_frame1
	.quad	LFB3-.
	.set L$set$6,LFE3-LFB3
	.quad L$set$6
	.byte	0
	.align 3
LEFDE5:
LSFDE7:
	.set L$set$7,LEFDE7-LASFDE7
	.long L$set$7
LASFDE7:
	.long	LASFDE7-EH_frame1
	.quad	LFB4-.
	.set L$set$8,LFE4-LFB4
	.quad L$set$8
	.byte	0
	.byte	0x4
	.set L$set$9,LCFI0-LFB4
	.long L$set$9
	.byte	0xe
	.byte	0x10
	.byte	0x4
	.set L$set$10,LCFI1-LCFI0
	.long L$set$10
	.byte	0xe
	.byte	0x8
	.align 3
LEFDE7:
LSFDE9:
	.set L$set$11,LEFDE9-LASFDE9
	.long L$set$11
LASFDE9:
	.long	LASFDE9-EH_frame1
	.quad	LFB5-.
	.set L$set$12,LFE5-LFB5
	.quad L$set$12
	.byte	0
	.byte	0x4
	.set L$set$13,LCFI2-LFB5
	.long L$set$13
	.byte	0xe
	.byte	0x10
	.byte	0x4
	.set L$set$14,LCFI3-LCFI2
	.long L$set$14
	.byte	0xe
	.byte	0x8
	.align 3
LEFDE9:
	.ident	"GCC: (Homebrew GCC 9.2.0) 9.2.0"
	.subsections_via_symbols
