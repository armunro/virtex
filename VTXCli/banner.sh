#!/bin/bash
export GIT_DISCOVERY_ACROSS_FILESYSTEM=1
commit_hash=$(git -C /root/virtex rev-parse --short HEAD) 
echo "Git: $commit_hash"
echo "                                             ";
echo " ██╗   ██╗██╗██████╗ ████████╗███████╗██╗  ██╗";
echo " ██║   ██║██║██╔══██╗╚══██╔══╝██╔════╝╚██╗██╔╝";
echo " ██║   ██║██║██████╔╝   ██║   █████╗   ╚███╔╝ ";
echo " ╚██╗ ██╔╝██║██╔══██╗   ██║   ██╔══╝   ██╔██╗ ";
echo "  ╚████╔╝ ██║██║  ██║   ██║   ███████╗██╔╝ ██╗";
echo "   ╚═══╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝";
echo "                                             ";