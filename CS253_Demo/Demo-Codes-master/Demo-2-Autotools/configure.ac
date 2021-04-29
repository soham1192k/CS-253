AC_INIT([hello],[1.0])
AC_PREREQ([2.68])
AM_INIT_AUTOMAKE([foreign])
AC_PROG_CC([vcc cl lcc gcc])
AC_PROG_CXX
AC_SUBST([FOO],[42])
AC_CONFIG_HEADERS([conf.h])
AC_CHECK_HEADERS([unistd.h])
AS_IF([test "$CC" = "gcc"],
    AC_DEFINE([SOEMTHING],[gcc],[Setting this for fun]),
    AC_DEFINE([SOMETHING],[42],[Setting this for fun]))
AC_PROG_AWK
AC_PROG_YACC
AC_PROG_GREP
AC_PROG_LEX
AC_CONFIG_FILES([Makefile])
AC_OUTPUT