Name:		texlive-fundus-calligra
Version:	26018
Release:	2
Summary:	Support for the calligra font in LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fundus/calligra
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fundus-calligra.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fundus-calligra.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fundus-calligra.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
