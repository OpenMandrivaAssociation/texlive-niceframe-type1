Name:		texlive-niceframe-type1
Version:	44671
Release:	1
Summary:	Type 1 versions of the fonts recommended in niceframe
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/niceframe-type1
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/niceframe-type1.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/niceframe-type1.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides Adobe Type 1 versions of the fonts
bbding10, dingbat, karta15, umranda and umrandb.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/type1/public/niceframe-type1
%{_texmfdistdir}/fonts/map/dvips/niceframe-type1
%{_texmfdistdir}/fonts/afm/public/niceframe-type1
%doc %{_texmfdistdir}/doc/fonts/niceframe-type1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
