# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/makeplot
# catalog-date 2008-01-20 02:03:54 +0100
# catalog-license lppl
# catalog-version 1.0.6
Name:		texlive-makeplot
Version:	1.0.6
Release:	4
Summary:	Easy plots from Matlab in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/makeplot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makeplot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makeplot.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makeplot.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0.6-2
+ Revision: 753733
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0.6-1
+ Revision: 718950
- texlive-makeplot
- texlive-makeplot
- texlive-makeplot
- texlive-makeplot

