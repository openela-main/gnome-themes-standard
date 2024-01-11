%global gtk2_version 2.24.15
%global gtk3_version 3.9.12

Name: gnome-themes-standard
Version: 3.22.3
Release: 4%{?dist}
Summary: Standard themes for GNOME applications

License: LGPLv2+
URL: http://git.gnome.org/browse/gnome-themes-standard
Source0: http://download.gnome.org/sources/%{name}/3.22/%{name}-%{version}.tar.xz
Source2: gtkrc


BuildRequires: gtk2-devel >= %{gtk2_version}
BuildRequires: gtk3-devel >= %{gtk3_version}
BuildRequires: librsvg2-devel
BuildRequires: intltool gettext autoconf automake libtool
BuildRequires: /usr/bin/gtk-update-icon-cache
Requires: abattis-cantarell-fonts
Requires: adwaita-gtk2-theme = %{version}-%{release}
Requires: adwaita-icon-theme

Conflicts: adwaita-gtk3-theme < 3.13.3

%description
The gnome-themes-standard package contains the standard theme for the GNOME
desktop, which provides default appearance for cursors, desktop background,
window borders and GTK+ applications.

%package -n adwaita-gtk2-theme
Summary: Adwaita gtk2 theme
Requires: gtk2%{_isa} >= %{gtk2_version}

%description -n adwaita-gtk2-theme
The adwaita-gtk2-theme package contains a gtk2 theme for presenting widgets
with a GNOME look and feel.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

rm -f $RPM_BUILD_ROOT%{_datadir}/icons/HighContrast/icon-theme.cache
touch $RPM_BUILD_ROOT%{_datadir}/icons/HighContrast/icon-theme.cache

rm $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.10.0/engines/libadwaita.la

mkdir -p $RPM_BUILD_ROOT%{_datadir}/gtk-2.0
cp $RPM_SOURCE_DIR/gtkrc $RPM_BUILD_ROOT%{_datadir}/gtk-2.0/gtkrc

%transfiletriggerin -- %{_datadir}/icons/HighContrast
gtk-update-icon-cache --force %{_datadir}/icons/HighContrast &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/HighContrast
gtk-update-icon-cache --force %{_datadir}/icons/HighContrast &>/dev/null || :

%files
%license COPYING
%doc NEWS
%dir %{_datadir}/icons/HighContrast
%{_datadir}/icons/HighContrast/16x16/
%{_datadir}/icons/HighContrast/22x22/
%{_datadir}/icons/HighContrast/24x24/
%{_datadir}/icons/HighContrast/32x32/
%{_datadir}/icons/HighContrast/48x48/
%{_datadir}/icons/HighContrast/256x256/
%{_datadir}/icons/HighContrast/scalable/
%{_datadir}/icons/HighContrast/index.theme
%ghost %{_datadir}/icons/HighContrast/icon-theme.cache
%{_datadir}/themes/Adwaita/gtk-3.0/
%{_datadir}/themes/Adwaita-dark/gtk-3.0/
%{_datadir}/themes/HighContrast/gtk-3.0/

%files -n adwaita-gtk2-theme
# gtk2 Theme and engine
%{_libdir}/gtk-2.0/2.10.0/engines/libadwaita.so
# Default gtk2 settings
%{_datadir}/gtk-2.0/gtkrc
%dir %{_datadir}/themes/Adwaita
%{_datadir}/themes/Adwaita/gtk-2.0/
%{_datadir}/themes/Adwaita/index.theme
%dir %{_datadir}/themes/Adwaita-dark
%{_datadir}/themes/Adwaita-dark/gtk-2.0/
%{_datadir}/themes/Adwaita-dark/index.theme
%dir %{_datadir}/themes/HighContrast
%{_datadir}/themes/HighContrast/gtk-2.0/
%{_datadir}/themes/HighContrast/index.theme

%changelog
* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Kalev Lember <klember@redhat.com> - 3.22.3-2
- Add file triggers for gtk-update-icon-cache

* Thu Mar 23 2017 David King <amigadave@amigadave.com> - 3.22.3-1
- Update to 3.22.3

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 12 2016 Kalev Lember <klember@redhat.com> - 3.22.2-1
- Update to 3.22.2
- Drop ancient obsoletes / provides

* Tue Oct 04 2016 Kalev Lember <klember@redhat.com> - 3.22.1-1
- Update to 3.22.1
- Don't set group tags
- Use make_install macro

* Sun May 15 2016 Kalev Lember <klember@redhat.com> - 3.20.2-1
- Update to 3.20.2

* Sun Apr 10 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 3.20-2
- Update default gtk-icon-theme-name (#1187409)

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20-1
- Update to 3.20

* Fri Mar 04 2016 Richard Hughes <rhughes@redhat.com> - 3.19.91-1
- Update to 3.19.91

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 22 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.2-1
- Update to 3.16.2
- Use license macro for the COPYING file

* Tue Mar 24 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Sat Feb 21 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.90-1
- Update to 3.15.90

* Fri Dec 19 2014 Richard Hughes <rhughes@redhat.com> - 3.15.2.2-1
- Update to 3.15.2.2

* Thu Nov 27 2014 Kalev Lember <kalevlember@gmail.com> - 3.15.2.1-1
- Update to 3.15.2.1

* Wed Nov 26 2014 Kalev Lember <kalevlember@gmail.com> - 3.15.2-1
- Update to 3.15.2

* Tue Nov 11 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.2-1
- Update to 3.14.2

* Tue Sep 23 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Tue Sep 02 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.90-2
- Conflict with older adwaita-gtk3-theme packages (#1133372)

* Fri Aug 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.90-1
- Update to 3.13.90

* Mon Aug 18 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.4-3
- Drop the default background image xml, moved over to gnome-backgrounds

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 21 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.4-1
- Update to 3.13.4

* Thu Jun 26 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.3-2
- Drop last references to adwaita-gtk3-theme
- Make gtk3 itself obsolete the adwaita-gtk3-theme package

* Thu Jun 26 2014 Richard Hughes <rhughes@redhat.com> - 3.13.3-1
- Update to 3.13.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 07 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.1-2
- Drop adwaita-cursor-theme subpackage, replaced by adwaita-icon-theme

* Mon Apr 28 2014 Richard Hughes <rhughes@redhat.com> - 3.13.1-1
- Update to 3.13.1

* Tue Mar 25 2014 Richard Hughes <rhughes@redhat.com> - 3.12.0-1
- Update to 3.12.0

* Thu Mar 20 2014 Matthias Clasen <mclasen@redhat.com> - 3.11.92-1
- Update to 3.11.92

* Fri Feb 21 2014 Matthias Clasen <mclasen@redhat.com> - 3.11.90-1
- Update to 3.11.90

* Thu Feb  6 2014 Debarshi Ray <rishi@fedoraproject.org> - 3.11.5-1
- Update to 3.11.5

* Mon Nov 25 2013 Richard Hughes <rhughes@redhat.com> - 3.11.2-1
- Update to 3.11.2

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Tue Sep  3 2013 Matthias Clasen <mclasen@redhat.com> - 3.9.91-1
- Update to 3.9.91

* Thu Aug 22 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.90-1
- Update to 3.9.90

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul  4 2013 Matthias Clasen <mclasen@redhat.com> - 3.9.3-3
- Move the packaged default gtk2 settings to /usr

* Thu Jul  4 2013 Matthias Clasen <mclasen@redhat.com> - 3.9.3-2
- Move the packaged default gtk3 settings to /usr

* Thu Jun 20 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.3-1
- Update to 3.9.3

* Mon Apr 15 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Tue Mar 19 2013 Richard Hughes <rhughes@redhat.com> - 3.7.92-1
- Update to 3.7.92

* Wed Mar  6 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Sun Feb 24 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.90-2
- Specify required gtk2 and gtk3 versions

* Wed Feb 20 2013 Richard Hughes <rhughes@redhat.com> - 3.7.90-1
- Update to 3.7.90

* Wed Feb 13 2013 Cosimo Cecchi <cosimoc@redhat.com> - 3.7.6-1
- Update to 3.7.6

* Thu Feb 07 2013 Richard Hughes <rhughes@redhat.com> - 3.7.5-1
- Update to 3.7.5

* Tue Jan 15 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.4-1
- Update to 3.7.4

* Thu Dec 20 2012 Kalev Lember <kalevlember@gmail.com> - 3.7.3-1
- Update to 3.7.3

* Tue Nov 20 2012 Richard Hughes <hughsient@gmail.com> - 3.7.2-1
- Update to 3.7.2

* Tue Nov 13 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.2-1
- Update to 3.6.2

* Mon Oct 15 2012 Cosimo Cecchi <cosimoc@redhat.com> - 3.6.1-1
- Update to 3.6.1

* Tue Oct  2 2012 Matthias Clasen <mclasen@redhat.com> - 3.6.0.2-2
- Drop gtk2-engines dependency

* Tue Sep 25 2012 Cosimo Cecchi <cosimoc@redhat.com> - 3.6.0.2-1
- Update to 3.6.0.2

* Wed Sep 19 2012 Richard Hughes <hughsient@gmail.com> - 3.5.92-1
- Update to 3.5.92

* Tue Sep 04 2012 Cosimo Cecchi <cosimoc@redhat.com> - 3.5.91-1
- Update to 3.5.91

* Tue Aug 21 2012 Cosimo Cecchi <cosimoc@redhat.com> - 3.5.90.1-1
- Update to 3.5.90.1

* Fri Aug 10 2012 Cosimo Cecchi <cosimoc@redhat.com> - 3.5.5-1
- Update to 3.5.5

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 17 2012 Richard Hughes <hughsient@gmail.com> - 3.5.4-1
- Update to 3.5.4

* Tue Jun 26 2012 Richard Hughes <hughsient@gmail.com> - 3.5.3-1
- Update to 3.5.3

* Thu Jun 07 2012 Richard Hughes <hughsient@gmail.com> - 3.5.2-1
- Update to 3.5.2

* Fri May 11 2012 Matthias Clasen <mclasen@redhat.com> - 3.5.1-2
- Fix handling of icon caches to be the same as elsewhere

* Sat May 05 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.1-1
- Update to 3.5.1

* Mon Apr 16 2012 Richard Hughes <hughsient@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Mon Mar 26 2012 Cosimo Cecchi <cosimoc@redhat.com> - 3.4.0-1
- Update to 3.4.0

* Tue Mar 20 2012 Cosimo Cecchi <cosimoc@redhat.com> - 3.3.92-1
- Update to 3.3.92

* Mon Mar  5 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.91-1
- Update to 3.3.91

* Sat Feb 25 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.90.1-1
- Update to 3.3.90.1

* Tue Feb  7 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.5.1-1
- Update to 3.3.5.1

* Mon Feb  6 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.5-1
- Update to 3.3.5

* Tue Jan 17 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.4-1
- Update to 3.3.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.3-1
- Update to 3.3.3

* Tue Nov 22 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.2-1
- Update to 3.3.2

* Wed Nov  2 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.1-1
- Update to 3.3.1

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for glibc bug#747377

* Tue Oct 18 2011 Matthias Clasen <mclasen@redhat.com> - 3.2.1-1
- Update to 3.2.1

* Wed Sep 28 2011 Ray <rstrode@redhat.com> - 3.2.0.2-1
- Update to 3.2.0.2

* Tue Sep 27 2011 Cosimo Cecchi <cosimoc@redhat.com> - 3.2.0.1-1
- Update to 3.2.0.1

* Mon Sep 26 2011 Ray <rstrode@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Mon Sep 19 2011 Cosimo Cecchi <cosimoc@redhat.com> - 3.1.92-1
- Update to 3.1.92

* Tue Sep  6 2011 Matthias Clasen <mclasen@redhat.com> 3.1.91-1
- Update to 3.1.91

* Tue Aug 30 2011 Matthias Clasen <mclasen@redhat.com> 3.1.90-1
- Update to 3.1.90
- Make more subpackage deps archful

* Tue Aug 16 2011 Matthias Clasen <mclasen@redhat.com> 3.1.5-1
- Update to 3.1.5

* Tue Aug 16 2011 Matthias Clasen <mclasen@redhat.com> 3.1.4-2
- Make the gtk2-engines dep arch-specific

* Mon Jul 25 2011 Matthias Clasen <mclasen@redhat.com> 3.1.4-1
- Update to 3.1.4

* Mon Jul 04 2011 Bastien Nocera <bnocera@redhat.com> 3.1.3-1
- Update to 3.1.3

* Tue Jun 14 2011 Cosimo Cecchi <cosimoc@redhat.com> - 3.1.2.1-1
- Update to 3.1.2.1

* Wed May 11 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.1-1
- Update to 3.1.1

* Mon Apr 25 2011 Matthias Clasen <mclasen@redhat.com> - 3.0.1-1
- Update to 3.0.1

* Mon Apr 18 2011 Adam Williamson <awilliam@redhat.com> - 3.0.0-4
- fix up the obsolete (thanks kk)

* Fri Apr 15 2011 Matthias Clasen <mclasen@redhat.com> - 3.0.0-3
- ...and do the provides/obsoletes dance too.

* Thu Apr 14 2011 Matthias Clasen <mclasen@redhat.com> - 3.0.0-2
- Drop gnome-themes-standard, apparently we loose the
  provides roulette again (#696832)

* Mon Apr 04 2011 Cosimo Cecchi <cosimoc@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Mon Mar 28 2011 Cosimo Cecchi <cosimoc@redhat.com> 2.91.93-3
- Don't make the cursor theme require gnome-themes-standard

* Mon Mar 28 2011 Cosimo Cecchi <cosimoc@redhat.com> 2.91.93-2
- Rebuild

* Mon Mar 28 2011 Cosimo Cecchi <cosimoc@redhat.com> 2.91.93-1
- Update to 2.91.93
- Make the cursor theme noarch
- Ship the default settings together with the relevant theme

* Mon Mar 28 2011 Ray Strode <rstrode@redhat.com> 2.91.92.1-4
- Fix Obsoletes

* Sat Mar 26 2011 Matthias Clasen <mclasen@redhat.com> 2.91.92.1-3
- Don't specify a nonexisting icon theme in settings.ini

* Thu Mar 24 2011 Matthias Clasen <mclasen@redhat.com> 2.91.92.1-2
- Add a subpackage for the default background

* Mon Mar 21 2011 Cosimo Cecchi <cosimoc@redhat.com> 2.91.92.1-1
- Update to 2.91.92.1

* Mon Mar 21 2011 Cosimo Cecchi <cosimoc@redhat.com> 2.91.92-1
- Update to 2.91.92

* Mon Mar 14 2011 Matthias Clasen <mclasen@redhat.com> 2.91.91.1-1
- Update to 2.91.91.1

* Mon Mar  7 2011 Matthias Clasen <mclasen@redhat.com> 2.91.91-1
- Update to 2.91.91

* Fri Mar 04 2011 Ray Strode <rstrode@redhat.com> 2.91.90-6
- Put COPYING and NEWS in correct place

* Fri Mar 04 2011 Ray Strode <rstrode@redhat.com> 2.91.90-5
- Drop icon-theme subpackage, it's empty

* Fri Mar 04 2011 Ray Strode <rstrode@redhat.com> 2.91.90-4
- Split out gtk themes into a subpackage as well
  Resolves: #675509

* Fri Mar 04 2011 Ray Strode <rstrode@redhat.com> 2.91.90-3
- Split cursors out into a subpackage
  Resolves: #675509

* Tue Feb 22 2011 Cosimo Cecchi <cosimoc@redha.com> - 2.91.90-2
- Fix insensitive checkboxes

* Tue Feb 22 2011 Matthias Clasen <mclasen@redhat.com> 2.91.90-1
- Update to 2.91.90

* Thu Feb 10 2011 Matthias Clasen <mclasen@redhat.com> 2.91.8-7
- Rebuild against newer gtk

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb  8 2011 Cosimo Cecchi <cosimoc@redhat.com> 2.91.8-4
- Pull in abattis-cantarell-fonts

* Fri Feb 04 2011 Ray Strode <rstrode@redhat.com> 2.91.8-3
- add gtkrc file for gtk2 apps
- take over fedora-gnome-theme's role

* Fri Feb  4 2011 Cosimo Cecchi <cosimoc@redhat.com> 2.91.8-2
- Add a patch from upstream for active toggle buttons

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> 2.91.8-1
- Update to 2.91.8
- Add default settings for session-less situations

* Sun Jan 23 2011 Matthias Clasen <mclasen@redhat.com> 2.91.7-1
- Update to 2.91.7

* Wed Jan 19 2011 Matthias Clasen <mclasen@redhat.com> 2.91.6-1
- Update to 2.91.6

* Mon Jan 10 2011 Matthias Clasen <mclasen@redhat.com> 2.91.5-1
- Update to 2.91.5

* Mon Nov 22 2010 Matthias Clasen <mclasen@redhat.com> 2.91.2.1-7
- Require gtk-theme-engine-clearlooks

* Tue Nov 16 2010 Matthias Clasen <mclasen@redhat.com> 2.91.2.1-6
- Obsoleting gnome-themes seems unnecessarily harsh

* Mon Nov 15 2010 Cosimo Cecchi <ccecchi@redhat.com> 2.91.2.1-5
- Add "Provides:" so that packages depending on gnome-themes don't break

* Mon Nov 15 2010 Cosimo Cecchi <ccecchi@redhat.com> 2.91.2.1-4
- Make this package obsolete gnome-themes

* Fri Nov 12 2010 Cosimo Cecchi <ccecchi@redhat.com> 2.91.2.1-3
- Make sure the theme directory is owned by the package too.
- Cleaned up the spec file a bit more to silence some rpmlint
  warnings.

* Fri Nov 12 2010 Cosimo Cecchi <ccecchi@redhat.com> 2.91.2.1-2
- Cleaned up the spec file, removed the %%clean section, and fixed a typo
  in the description.

* Fri Nov 12 2010 Cosimo Cecchi <ccecchi@redhat.com> 2.91.2.1-1
- First packaging of gnome-themes-standard
