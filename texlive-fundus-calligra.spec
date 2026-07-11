%global tl_name fundus-calligra
%global tl_revision 79063

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.11
Release:	%{tl_revision}.1
Summary:	Support for the calligra font in LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fundus/calligra
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fundus-calligra.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fundus-calligra.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fundus-calligra.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package offers support for the calligra handwriting font, in LaTeX
documents. The package is part of the fundus bundle.

