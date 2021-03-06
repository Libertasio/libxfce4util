#!/usr/bin/env python3

# You can generate python documentation with the following commands:
# g-ir-doc-tool --language Python -o ./html ../libxfce4util/libxfce4util-1.0.gir
# yelp ./html/

import gi.repository
# Set the search path to use the newly generated introspection files
gi.require_version('GIRepository', '2.0')
from gi.repository import GIRepository
GIRepository.Repository.prepend_search_path('../libxfce4util/')
# Now import 4util
gi.require_version('libxfce4util', '1.0')
from gi.repository import libxfce4util

# print out some stuff to see if it works
print("homedir: ", libxfce4util.get_homedir())
print("get_dir_localized: ", libxfce4util.get_dir_localized(libxfce4util.get_homedir()))
print("version: ", libxfce4util.version_string())
