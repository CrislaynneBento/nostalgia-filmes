import subprocess
import gi
gi.require_version('Gedit', '3.0')
from gi.repository import GObject, Gedit, Gtk

#1. Inicializando com uma classe que permite a entrada de uma janela 
#no Pluma, que lerá o que foi digitado pelo professor. 
class OrcaSpellPlugin(GObject.Object, Gedit.WindowActivatable):
    __gtype_name__ = "OrcaSpellPlugin"
    window = GObject.Property(type=Gedit.Window)

    def __init__ (self):
        GObject.Object.__init__(self)
        self.erros = []
        self.indice = 0

        #primeiro método rodará quando o professor ativa o plugin nas configurações do pluma
        def do_activate(self):
            self._adicionar_atalhos()

        #segundo método rodará quando o professor desativar o plugin
        def do_deactivate(self):
            pass
        
        #terceiro método rodará toda vez que o estado da janela mudar.
        def do_update_state(self):
            pass



