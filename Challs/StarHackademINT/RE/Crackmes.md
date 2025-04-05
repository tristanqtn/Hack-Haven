# Crackme [1/3]

We start by checking the file signature : 

```bash
file crackme1
crackme1: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, not stripped
```

Then we extract the constant strings from the binary : 

```bash
strings crackme1
```

And we get the flag because it's an easy one : 

```plaintext
/lib64/ld-linux-x86-64.so.2
exit
__libc_start_main
printf
strcmp
libc.so.6
GLIBC_2.2.5
GLIBC_2.34
__gmon_start__
PTE1
H=(@@
Usage : ./crackme1 [PASSWORD]
Star{Viv3_les_Pokes_et_La-LIBC}
Too Bad...
;*3$"
GCC: (GNU) 14.2.0
crt1.o
__abi_tag
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.0
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
source.c
__FRAME_END__
_DYNAMIC
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
__libc_start_main@GLIBC_2.34
_edata
_fini
printf@GLIBC_2.2.5
__data_start
strcmp@GLIBC_2.2.5
__gmon_start__
__dso_handle
_IO_stdin_used
_end
_dl_relocate_static_pie
__bss_start
main
exit@GLIBC_2.2.5
__TMC_END__
_init
.symtab
.strtab
.shstrtab
.interp
.note.gnu.property
.note.ABI-tag
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rela.dyn
.rela.plt
.init
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.init_array
.fini_array
.dynamic
.got
.got.plt
.data
.bss
.comment
```

Flag : `Star{Viv3_les_Pokes_et_La-LIBC}`

# Crackme [2/3]

This second crackme is a bit different. We decompile the file using https://dogbolt.org/ because the file is super lightweight. Here's a part of the password verification function : 

```c
void __fastcall __noreturn main(int a1, char **a2, char **a3)
{
  if ( a1 <= 1 )
  {
    printf("Usage : ./crackme2 [PASSWORD]");
    exit(1);
  }
  if ( strlen(a2[1]) != 83 )
  {
    printf("Too Bad...");
    exit(0);
  }
  if ( a2[1][33] != 95 )
  {
    printf("Too Bad...");
    exit(0);
  }
  if ( a2[1][19] != 95 )
  {
    printf("Too Bad...");
    exit(0);
  }
  if ( a2[1][42] != 114 )
  {
    printf("Too Bad...");
    exit(0);
  }
```

The password is received by the program as argument, then sent to the verification function. This function first checks if an argument has been provided : 

```c
if ( a1 <= 1 )
  {
    printf("Usage : ./crackme2 [PASSWORD]");
    exit(1);
  }
```

Then checks the length of the given password, it should be 83 characters long without the escape character `\n`. 

```c
if ( strlen(a2[1]) != 83 )
  {
    printf("Too Bad...");
    exit(0);
  }
```

Then for each character position of the password, the function tests if the character is equal to an ASCII character. If the character is different we're kicked out of the program. Using the following table we reorder the character and find the flag using the ASCII table equivalences.  

|Position|ASCII|Character|
|---|---|---|
|0|83|'S'|
|1|116|'t'|
|2|97|'a'|
|3|114|'r'|
|4|123|'{'|
|5|49|'1'|
|6|108|'l'|
|7|95|'_'|
|8|121|'y'|
|9|95|'_'|
|10|51|'3'|
|11|110|'n'|
|12|95|'_'|
|13|97|'a'|
|14|95|'_'|
|15|112|'p'|
|16|108|'l'|
|17|85|'U'|
|18|115|'s'|
|19|95|'_'|
|20|100|'d'|
|21|101|'e'|
|22|95|'_'|
|23|49|'1'|
|24|53|'5'|
|25|48|'0'|
|26|95|'_'|
|27|81|'Q'|
|28|117|'u'|
|29|51|'3'|
|30|95|'_'|
|31|116|'t'|
|32|85|'U'|
|33|95|'_'|
|34|80|'P'|
|35|51|'3'|
|36|117|'u'|
|37|120|'x'|
|38|95|'_'|
|39|52|'4'|
|40|116|'t'|
|41|116|'t'|
|42|114|'r'|
|43|97|'a'|
|44|112|'p'|
|45|51|'3'|
|46|114|'r'|
|47|33|'!'|
|48|33|'!'|
|49|33|'!'|
|50|33|'!'|
|51|33|'!'|
|52|32|' '|
|53|40|'('|
|54|98|'b'|
|55|111|'o'|
|56|110|'n'|
|57|32|' '|
|58|108|'l'|
|59|97|'a'|
|60|32|' '|
|61|106|'j'|
|62|39|"'"|
|63|101|'e'|
|64|110|'n'|
|65|32|' '|
|66|97|'a'|
|67|105|'i'|
|68|32|' '|
|69|109|'m'|
|70|105|'i'|
|71|115|'s'|
|72|32|' '|
|73|109|'m'|
|74|111|'o'|
|75|105|'i'|
|76|110|'n'|
|77|115|'s'|
|78|46|'.'|
|79|46|'.'|
|80|46|'.'|
|81|41|')'|
|82|125|'}'|
Flag : `Star{1l_y_3n_a_plUs_de_150_Qu3_tU_P3ux_4ttrap3r!!!!! (bon la j'en ai mis moins...)}`