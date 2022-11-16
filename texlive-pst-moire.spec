Name:		texlive-pst-moire
Version:	60411
Release:	1
Summary:	A PSTricks package to draw moire patterns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pst-moire
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-moire.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-moire.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a PSTricks package to draw moire patterns.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pst-moire
%{_texmfdistdir}/tex/generic/pst-moire
%{_texmfdistdir}/dvips/pst-moire
%doc %{_texmfdistdir}/doc/generic/pst-moire

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
