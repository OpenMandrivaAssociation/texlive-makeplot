# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/makeplot
# catalog-date 2008-01-20 02:03:54 +0100
# catalog-license lppl
# catalog-version 1.0.6
Name:		texlive-makeplot
Version:	1.0.6
Release:	1
Summary:	Easy plots from Matlab in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/makeplot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makeplot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makeplot.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makeplot.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Existing approaches to create EPS files from Matlab (laprint,
mma2ltx, print -eps, etc.) aren't satisfactory; makeplot aims
to resolve this problem. Makeplot is a LaTeX package that uses
the pstricks pst-plot functions to plot data that it takes from
Matlab output files.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
