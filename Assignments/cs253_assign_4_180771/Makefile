.SILENT: all
SHELL=bash
all: build
build: run.sh code.cpp code_without_vulnerabilities1.cpp code_without_vulnerabilities2.cpp code_without_vulnerabilities3.cpp
	@$(SHELL) $<
clean: 
	@rm -rf *.out 