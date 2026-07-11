%global tl_name niceframe-type1
%global tl_revision 71849

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Type 1 versions of the fonts recommended in niceframe
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/niceframe
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/niceframe-type1.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/niceframe-type1.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides Adobe Type 1 versions of the fonts bbding10,
dingbat, karta15, umranda and umrandb.

