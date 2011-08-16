Summary:	mscgen filter for AsciiDoc
Summary(pl.UTF-8):	Filtr mscgen do narzędzia AsciiDoc
Name:		asciidoc-filter-mscgen
Version:	1.2
Release:	1
License:	GPL v2
Group:		Applications/Graphics
#Source0Download: http://code.google.com/p/asciidoc-mscgen-filter/downloads/list
Source0:	http://asciidoc-mscgen-filter.googlecode.com/files/mscgen-filter-%{version}.zip
# Source0-md5:	418b94e32bd247c3e93bfe0a3b55fee6
URL:		http://code.google.com/p/asciidoc-mscgen-filter/
BuildRequires:	unzip
Requires:	asciidoc >= 8.6.5
# should be 0.21, but not released yet
Requires:	mscgen >= 0.20
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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/asciidoc/filters/mscgen

install filter-wrapper.py $RPM_BUILD_ROOT/etc/asciidoc/filters/mscgen
cp -p mscgen-filter.conf $RPM_BUILD_ROOT/etc/asciidoc/filters/mscgen

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc asciidoc-mscgen-readme.{txt,html} images
%dir /etc/asciidoc/filters/mscgen
%attr(755,root,root) /etc/asciidoc/filters/mscgen/filter-wrapper.py
/etc/asciidoc/filters/mscgen/mscgen-filter.conf
