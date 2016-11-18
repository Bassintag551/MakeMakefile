#!/usr/bin/python


import os
import sys
import time

def main():
    dest = open("Makefile", "w")
    args = sys.argv
    if len(args) < 3:
        print("Usage: MakeMakefile [name] (-l/) [source files...]")
    else:
        login = os.getlogin()
        name = login.replace(".", " ").title()
        date = time.strftime("%c")
        libs = False
        srcs = []
        for index in range(2, len(args)):
            if args[index] == "-l":
                libs = True
            else:
                srcs.append(args[index])
        dest.write("##\n")
        dest.write("## Makefile for " + args[1] + " in " + str(os.getcwd()) + "\n")
        dest.write("##\n")
        dest.write("## Made by " + name + "\n")
        dest.write("## Login   <" + login + "@epitech.eu>\n")
        dest.write("##\n")
        dest.write("## Started on  " + date + " " + name + "\n")
        dest.write("## Last update " + date + " " + name + "\n")
        dest.write("##\n\n")
        dest.write("CC\t=\tgcc\n\n")
        dest.write("RM\t=\trm -f\n\n")
        dest.write("CFLAGS\t=\t-Wextra -Wall -Werror -I $(INC)\n\n")
        dest.write("LDFLAGS\t=\n\n")
        dest.write("INC\t=\tinclude\n\n")
        if libs:
            dest.write("LIBDIR\t=\tlib\n\n")
            dest.write("LIB\t=\n\n")
        dest.write("NAME\t=\t" + args[1] + "\n\n")
        dest.write("OBJS\t=\t$(SRCS:.c=.o)\n\n")
        dest.write("SRCS\t=\t")
        for index in range(0 ,len(srcs)):
            dest.write(("\t\t" if index > 0 else "") + srcs[index] + (" \\\n" if index < len(srcs) - 1 else "\n\n"))
        dest.write("all: $(NAME)\n\n")
        dest.write("$(NAME): $(OBJS)\n\t$(CC) $(OBJS) -o $(NAME) $(LDFLAGS)" + ("  -L $(LIBDIR) -l $(LIB)\n\n" if libs else "\n\n"))
        dest.write("clean:\n\t$(RM) $(OBJS)\n\n")
        dest.write("fclean: clean\n\t$(RM) $(NAME)\n\n")
        dest.write("re: clean all\n\n")
        dest.write(".PHONY: all clean fclean re")
        dest.close()
        print("Successfully generated Makefile!")

if __name__ == "__main__":
    main()
