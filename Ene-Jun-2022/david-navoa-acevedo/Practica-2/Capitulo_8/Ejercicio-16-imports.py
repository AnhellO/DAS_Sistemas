import imp
import SeparatedFile 
SeparatedFile.display_message()

from SeparatedFile import display_message


from SeparatedFile import display_message as dm
dm()

import SeparatedFile as sp
sp.display_message()

from SeparatedFile import *
display_message()