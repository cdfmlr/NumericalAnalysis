	.text
	.p2align 4
	.globl _algo_1
_algo_1:
LFB1:
	testl	%edi, %edi
	je	L7
	movsd	lC1(%rip), %xmm3
	pxor	%xmm2, %xmm2
	movsd	lC3(%rip), %xmm4
	movapd	%xmm3, %xmm0
	.p2align 4,,10
	.p2align 3
L2:
	pxor	%xmm1, %xmm1
	cvtsi2sdl	%edi, %xmm1
	movapd	%xmm3, %xmm5
	subl	$1, %edi
	divsd	%xmm1, %xmm5
	movapd	%xmm5, %xmm1
	mulsd	%xmm0, %xmm1
	mulsd	%xmm4, %xmm0
	addsd	%xmm1, %xmm2
	jne	L2
	mulsd	lC0(%rip), %xmm0
	addsd	%xmm2, %xmm0
	ret
	.p2align 4,,10
	.p2align 3
L7:
	movsd	lC0(%rip), %xmm0
	ret
LFE1:
	.p2align 4
	.globl _algo_2
_algo_2:
LFB2:
	cmpl	$100, %edi
	je	L13
	movsd	lC1(%rip), %xmm0
	pxor	%xmm2, %xmm2
	movsd	lC5(%rip), %xmm4
	movsd	lC6(%rip), %xmm3
	.p2align 4,,10
	.p2align 3
L9:
	pxor	%xmm1, %xmm1
	cvtsi2sdl	%edi, %xmm1
	movapd	%xmm4, %xmm5
	addl	$1, %edi
	cmpl	$100, %edi
	divsd	%xmm1, %xmm5
	movapd	%xmm5, %xmm1
	mulsd	%xmm0, %xmm1
	mulsd	%xmm3, %xmm0
	addsd	%xmm1, %xmm2
	jne	L9
	mulsd	lC4(%rip), %xmm0
	addsd	%xmm2, %xmm0
	ret
	.p2align 4,,10
	.p2align 3
L13:
	movsd	lC4(%rip), %xmm0
	ret
LFE2:
	.cstring
	.align 3
lC10:
	.ascii "algo_1: I(n) = 1 / n - 5 * I(n - 1)\0"
	.align 3
lC11:
	.ascii "algo_2: I(n) = (1 / n - I(n + 1)) / 5\12\0"
lC12:
	.ascii "accuracy: I(%d) = %f\12\0"
lC13:
	.ascii "algo_1: %f\12\0"
lC14:
	.ascii "algo_2: %f\12\12\0"
	.section __TEXT,__text_startup,regular,pure_instructions
	.p2align 4
	.globl _main
_main:
LFB3:
	pushq	%r13
LCFI0:
	leaq	lC10(%rip), %rdi
	pushq	%r12
LCFI1:
	pushq	%rbp
LCFI2:
	xorl	%ebp, %ebp
	pushq	%rbx
LCFI3:
	subq	$56, %rsp
LCFI4:
	movdqa	lC7(%rip), %xmm0
	leaq	16(%rsp), %r12
	movq	%rsp, %r13
	movaps	%xmm0, (%rsp)
	movapd	lC8(%rip), %xmm0
	movaps	%xmm0, 16(%rsp)
	movapd	lC9(%rip), %xmm0
	movaps	%xmm0, 32(%rsp)
	call	_puts
	leaq	lC11(%rip), %rdi
	call	_puts
L20:
	movl	0(%r13,%rbp,4), %ebx
	leaq	lC12(%rip), %rdi
	movl	$1, %eax
	movsd	(%r12,%rbp,8), %xmm0
	movl	%ebx, %esi
	call	_printf
	movq	lC1(%rip), %rax
	testl	%ebx, %ebx
	movq	%rax, %xmm3
	movq	lC3(%rip), %rax
	movq	%rax, %xmm4
	je	L15
	movl	%ebx, %eax
	movapd	%xmm3, %xmm0
	pxor	%xmm2, %xmm2
	.p2align 4,,10
	.p2align 3
L16:
	pxor	%xmm1, %xmm1
	cvtsi2sdl	%eax, %xmm1
	movapd	%xmm3, %xmm7
	subl	$1, %eax
	divsd	%xmm1, %xmm7
	movapd	%xmm7, %xmm1
	mulsd	%xmm0, %xmm1
	mulsd	%xmm4, %xmm0
	addsd	%xmm1, %xmm2
	jne	L16
	mulsd	lC0(%rip), %xmm0
	movl	$1, %eax
	leaq	lC13(%rip), %rdi
	addsd	%xmm2, %xmm0
	call	_printf
	movq	lC1(%rip), %rax
	cmpl	$100, %ebx
	movq	%rax, %xmm3
	movq	lC5(%rip), %rax
	movq	%rax, %xmm6
	movq	lC6(%rip), %rax
	movq	%rax, %xmm5
	je	L30
L18:
	movapd	%xmm3, %xmm0
	pxor	%xmm2, %xmm2
	.p2align 4,,10
	.p2align 3
L22:
	pxor	%xmm1, %xmm1
	cvtsi2sdl	%ebx, %xmm1
	movapd	%xmm6, %xmm7
	addl	$1, %ebx
	cmpl	$100, %ebx
	divsd	%xmm1, %xmm7
	movapd	%xmm7, %xmm1
	mulsd	%xmm0, %xmm1
	mulsd	%xmm5, %xmm0
	addsd	%xmm1, %xmm2
	jne	L22
L17:
	leaq	lC14(%rip), %rdi
	movl	$1, %eax
	addq	$1, %rbp
	mulsd	lC4(%rip), %xmm0
	addsd	%xmm2, %xmm0
	call	_printf
	cmpq	$4, %rbp
	jne	L20
	addq	$56, %rsp
LCFI5:
	xorl	%eax, %eax
	popq	%rbx
LCFI6:
	popq	%rbp
LCFI7:
	popq	%r12
LCFI8:
	popq	%r13
LCFI9:
	ret
L15:
LCFI10:
	movq	lC0(%rip), %rax
	leaq	lC13(%rip), %rdi
	movq	%rax, %xmm0
	movl	$1, %eax
	call	_printf
	movq	lC1(%rip), %rax
	movq	%rax, %xmm3
	movq	lC5(%rip), %rax
	movq	%rax, %xmm6
	movq	lC6(%rip), %rax
	movq	%rax, %xmm5
	jmp	L18
L30:
	movapd	%xmm3, %xmm0
	pxor	%xmm2, %xmm2
	jmp	L17
LFE3:
	.literal8
	.align 3
lC0:
	.long	1023920203
	.long	1070028187
	.align 3
lC1:
	.long	0
	.long	1072693248
	.align 3
lC3:
	.long	0
	.long	-1072431104
	.align 3
lC4:
	.long	1763341773
	.long	1063107753
	.align 3
lC5:
	.long	2576980378
	.long	1070176665
	.align 3
lC6:
	.long	2576980378
	.long	-1077306983
	.literal16
	.align 4
lC7:
	.long	8
	.long	10
	.long	12
	.long	14
	.align 4
lC8:
	.long	4285346569
	.long	1066617546
	.long	1297423721
	.long	1066366224
	.align 4
lC9:
	.long	4003596715
	.long	1066045443
	.long	366962006
	.long	1065811905
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
	.byte	0x4
	.set L$set$7,LCFI0-LFB3
	.long L$set$7
	.byte	0xe
	.byte	0x10
	.byte	0x8d
	.byte	0x2
	.byte	0x4
	.set L$set$8,LCFI1-LCFI0
	.long L$set$8
	.byte	0xe
	.byte	0x18
	.byte	0x8c
	.byte	0x3
	.byte	0x4
	.set L$set$9,LCFI2-LCFI1
	.long L$set$9
	.byte	0xe
	.byte	0x20
	.byte	0x86
	.byte	0x4
	.byte	0x4
	.set L$set$10,LCFI3-LCFI2
	.long L$set$10
	.byte	0xe
	.byte	0x28
	.byte	0x83
	.byte	0x5
	.byte	0x4
	.set L$set$11,LCFI4-LCFI3
	.long L$set$11
	.byte	0xe
	.byte	0x60
	.byte	0x4
	.set L$set$12,LCFI5-LCFI4
	.long L$set$12
	.byte	0xa
	.byte	0xe
	.byte	0x28
	.byte	0x4
	.set L$set$13,LCFI6-LCFI5
	.long L$set$13
	.byte	0xe
	.byte	0x20
	.byte	0x4
	.set L$set$14,LCFI7-LCFI6
	.long L$set$14
	.byte	0xe
	.byte	0x18
	.byte	0x4
	.set L$set$15,LCFI8-LCFI7
	.long L$set$15
	.byte	0xe
	.byte	0x10
	.byte	0x4
	.set L$set$16,LCFI9-LCFI8
	.long L$set$16
	.byte	0xe
	.byte	0x8
	.byte	0x4
	.set L$set$17,LCFI10-LCFI9
	.long L$set$17
	.byte	0xb
	.align 3
LEFDE5:
	.ident	"GCC: (Homebrew GCC 9.2.0) 9.2.0"
	.subsections_via_symbols
