%global tl_name makeplot
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.6
Release:	%{tl_revision}.1
Summary:	Easy plots from Matlab in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/makeplot
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makeplot.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makeplot.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makeplot.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Existing approaches to create EPS files from Matlab (laprint, mma2ltx,
print -eps, etc.) aren't satisfactory; makeplot aims to resolve this
problem. Makeplot is a LaTeX package that uses the pstricks pst-plot
functions to plot data that it takes from Matlab output files.

