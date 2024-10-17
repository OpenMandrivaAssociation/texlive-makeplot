Name:		texlive-makeplot
Version:	15878
Release:	2
Summary:	Easy plots from Matlab in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/makeplot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makeplot.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makeplot.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makeplot.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Existing approaches to create EPS files from Matlab (laprint,
mma2ltx, print -eps, etc.) aren't satisfactory; makeplot aims
to resolve this problem. Makeplot is a LaTeX package that uses
the pstricks pst-plot functions to plot data that it takes from
Matlab output files.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/makeplot/makeplot.sty
%doc %{_texmfdistdir}/doc/latex/makeplot/README
%doc %{_texmfdistdir}/doc/latex/makeplot/data1.mat
%doc %{_texmfdistdir}/doc/latex/makeplot/data2.mat
%doc %{_texmfdistdir}/doc/latex/makeplot/makeplot.pdf
%doc %{_texmfdistdir}/doc/latex/makeplot/mptest.tex
#- source
%doc %{_texmfdistdir}/source/latex/makeplot/makeplot.dtx
%doc %{_texmfdistdir}/source/latex/makeplot/makeplot.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
