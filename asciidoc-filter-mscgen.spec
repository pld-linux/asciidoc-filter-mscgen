Summary:	mscgen filter for AsciiDoc
Summary(pl.UTF-8):	Filtr mscgen do narzędzia AsciiDoc
Name:		asciidoc-filter-mscgen
Version:	1.2
Release:	4
License:	GPL v2
Group:		Applications/Graphics
#Source0Download: https://github.com/hwmaier/asciidoc-mscgen-filter/tags
Source0:	http://asciidoc-mscgen-filter.googlecode.com/files/mscgen-filter-%{version}.zip
# Source0-md5:	418b94e32bd247c3e93bfe0a3b55fee6
URL:		https://github.com/hwmaier/asciidoc-mscgen-filter
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	asciidoc >= 8.6.5
# should be 0.21, but not released yet
Requires:	mscgen >= 0.20
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Using the AsciiDoc mscgen filter, Message Sequence Chart descriptions
can be embedded into AsciiDoc documents and processed into either PNG
bitmap or SVG vector graphics.

%description -l pl.UTF-8
Przy użyciu filtra mscgen do AsciiDoc można osadzać opisy Message
Sequence Chart (wykresów sekwencji komunikatów) w dokumentach AsciiDoc
i przetwarzać je do formatu bitmap PNG lub grafik wektorowych SVG.

%prep
%setup -q -c

%{__sed} -i -e '1s,/usr/bin/env python,%{__python3},' filter-wrapper.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py3_sitescriptdir}/asciidoc/resources/filters/mscgen

install filter-wrapper.py $RPM_BUILD_ROOT%{py3_sitescriptdir}/asciidoc/resources/filters/mscgen
cp -p mscgen-filter.conf $RPM_BUILD_ROOT%{py3_sitescriptdir}/asciidoc/resources/filters/mscgen
%py3_comp $RPM_BUILD_ROOT%{py3_sitescriptdir}/asciidoc/resources/filters/mscgen
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitescriptdir}/asciidoc/resources/filters/mscgen

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc asciidoc-mscgen-readme.{txt,html} images
%dir %{py3_sitescriptdir}/asciidoc/resources/filters/mscgen
%attr(755,root,root) %{py3_sitescriptdir}/asciidoc/resources/filters/mscgen/filter-wrapper.py
%{py3_sitescriptdir}/asciidoc/resources/filters/mscgen/__pycache__
%{py3_sitescriptdir}/asciidoc/resources/filters/mscgen/mscgen-filter.conf
