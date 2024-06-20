#!/usr/bin/perl

# perl check_file_exist.pl
# Perl中-e操作符用于检测文件是否存在
use strict;
use warnings;

my $file = "./a.txt";
if (-e $file) {
    print "$file exists.\n";
} else {
    print "$file does not exist.\n";
}
