# revision 26018
# category Package
# catalog-ctan /macros/latex/contrib/fundus/calligra
# catalog-date 2012-04-15 00:54:55 +0200
# catalog-license other-free
# catalog-version 1.2
Name:		texlive-fundus-calligra
Version:	1.2
Release:	9
Summary:	Support for the calligra font in LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fundus/calligra
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fundus-calligra.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fundus-calligra.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fundus-calligra.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers support for the calligra handwriting font,
in LaTeX documents. The package is part of the fundus bundle.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fundus-calligra/calligra.sty
%doc %{_texmfdistdir}/doc/latex/fundus-calligra/calligra.pdf
#- source
%doc %{_texmfdistdir}/source/latex/fundus-calligra/calligra.dtx
%doc %{_texmfdistdir}/source/latex/fundus-calligra/calligra.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 813540
- Update to latest release.
- Import texlive-fundus-calligra
- Import texlive-fundus-calligra

