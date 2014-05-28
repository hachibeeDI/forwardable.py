# -*- coding: utf-8 -*-

from operator import methodcaller


class Forwardable(type):

    def __init__(cls, name, bases, dct):
        super(Forwardable, cls).__init__(name, bases, dct)
        delegation_defs = [(methodname, v) for (methodname, v) in dct.iteritems() if isinstance(v, (def_delegator, def_delegators, ))]
        for methodname, delegator in delegation_defs:
            delattr(cls, methodname)
            delegator.apply_delegate_definition(cls, methodname)


class def_delegator(object):
    __slots__ = ('accesor', 'proxy', )

    def __init__(self, accesor, proxy=None):
        self.accesor = accesor
        self.proxy = proxy

    def apply_delegate_definition(self, cls, methodname):
        # print('state method: {}, accesor: {}, proxy: {}'.format(methodname, self.accesor, self.proxy, ))
        if self.proxy is None:
            setattr(cls, methodname, self.delegation_method_builder(methodname))
        else:
            setattr(cls, methodname, self.proxy_method_builder())

    def delegation_method_builder(self, methodname):
        accesor_name = self.accesor

        def _method(self, *args, **kw):
            delegate_target = getattr(self, accesor_name)
            accesor_method = methodcaller(methodname, *args, **kw)
            return accesor_method(delegate_target)
        return _method

    def proxy_method_builder(self):
        accesor_name = self.accesor
        methodname = self.proxy

        def _method(self, *args, **kw):
            delegate_target = getattr(self, accesor_name)
            accesor_method = methodcaller(methodname, *args, **kw)
            return accesor_method(delegate_target)
        return _method



class def_delegators(object):
    __slots__ = ('accesor', 'delegations', 'proxy', )

    def __init__(self, accesor, delegations, proxy=None):
        self.accesor = accesor
        self.delegations = delegations
        self.proxy = proxy

    def apply_delegate_definition(self, cls, _=None):
        for defs in self.delegations:
            setattr(cls, defs, self.delegation_method_builder(defs))

    def delegation_method_builder(self, methodname):
        accesor_name = self.accesor

        def _method(self, *args, **kw):
            delegate_target = getattr(self, accesor_name)
            accesor_method = methodcaller(methodname, *args, **kw)
            return accesor_method(delegate_target)
        return _method
