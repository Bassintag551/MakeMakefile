#!/usr/bin/python

import sys

def main():
    dest = open("Makefile", "w")
    args = sys.argv
    if len(args) < 3:
        print("Usage: MakeMakefile [name] [source files...]")
    else:
        dest.write("\nCC\t=\tgcc\n\n")
        dest.write("RM\t=\trm -f\n\n")
        dest.write("CFLAGS\t=\t-Wextra -Wall -Werror\n\n")
        dest.write("LDFLAGS\t=\n\n")
        dest.write("INC\t=\tinclude\n\n")
        dest.write("NAME\t=\t" + args[1] + "\n\n")
        dest.write("OBJS\t=\t$(SRCS:.c=.o)\n\n")
        dest.write("SRCS\t=\t")
        for index in range(2,len(args)):
            dest.write(("\t\t" if index > 2 else "") + args[index] + (" \\\n" if index < len(args) - 1 else "\n\n"))
        dest.write("all: $(NAME)\n\n")
        dest.write("$(NAME): $(OBJS)\n\t$(CC) $(OBJS) -I $(INC) -o $(NAME) $(LDFLAGS)\n\n")
        dest.write("clean:\n\t$(RM) $(OBJS)\n\n")
        dest.write("fclean: clean\n\t$(RM) $(NAME)\n\n")
        dest.write("re: clean all\n\n")
        dest.write(".PHONY: all clean fclean re")
        dest.close()
        print("Successfully generated Makefile, don't forget to add your header")

if __name__ == "__main__":
    main()
