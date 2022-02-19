#!/usr/bin/python3
import shutil, os, sys, pkgutil

major = 0
minor = 0
patch = 0

patch_terms = {"(balance)", "(bugfix)", "(refactor)"}
minor_terms = {"(char-rework)", "(feature)"}
major_terms = {"(major)"}


merge_lines = []
for line in pkgutil.run_command("git log --oneline").split("\n"):
    if "Merge pull request #" in line:
        hash = line.split(" ", 1)[0]
    
        commit_body = pkgutil.run_command("git log -n 1 --pretty=format:%b " + hash)

        if any(major_term in commit_body for major_term in major_terms):
            major += 1
            minor = 0
            patch = 0
            print(commit_body)
            print(str(major) + "." + str(minor) + "." + str(patch))
        elif any(minor_term in commit_body for minor_term in minor_terms):
            minor += 1
            patch = 0
            print(commit_body)
            print(str(major) + "." + str(minor) + "." + str(patch))
        elif any(patch_term in commit_body for patch_term in patch_terms):
            patch += 1
            print(commit_body)
            print(str(major) + "." + str(minor) + "." + str(patch))

print("final:")
print(str(major) + "." + str(minor) + "." + str(patch))

