class MetaEnumType(type):
    def __init__(cls, name, bases, attrs):
        reverse_name, reverse_verbose, _by_name, _by_verbose = {}, {}, {}, {}
        for name, item in attrs.items():
            if not name.startswith('__'):
                if type(item)==tuple:
                    value, verbose = item
                else:
                    value = item
                    verbose = unicode(item)

                setattr(cls, name+'_verbose', verbose)
                setattr(cls, name+'_name', name)
                setattr(cls, name, value)
                reverse_name[value] = name
                reverse_verbose[value] = verbose
                _by_name[name] = value
                _by_verbose[verbose] = value

        # attrs: name, verbose
        setattr(cls, 'name', reverse_name)
        setattr(cls, 'verbose', reverse_verbose)

        # functions: get_name, verbose
        get_name = classmethod(lambda cls,v: reverse_name[v])

        def _get_verbose(cls,v):
            try:
                return reverse_verbose[v]
            except KeyError, e:
                raise Exception('KeyError: MetaEnum "%s" has no value "%s"!'%(cls.__name__, v) )

        get_verbose = classmethod( _get_verbose )
        setattr(cls, 'get_name', get_name)
        setattr(cls, 'get_verbose', get_verbose)

        # by_name, by_verbose
        setattr(cls, 'by_name', staticmethod( lambda name: _by_name[name] ) )
        setattr(cls, 'by_verbose', staticmethod( lambda verbose: _by_verbose[verbose] ) )

        setattr(cls, 'verbose_by_int', staticmethod( lambda value: reverse_verbose[value]) )
        # utilit functions: as_choices
        choices = [ (k,v) for k,v in reverse_verbose.iteritems() ]
        as_choices = staticmethod(lambda : choices )
        setattr(cls, 'as_choices', as_choices)

        # revesred (with_none)
        choices_vk = [ (v,k) for k,v in reverse_verbose.iteritems() ]
        as_choices_vk = staticmethod(lambda with_none=False: choices_vk if not with_none else [ ('',None) ]+choices_vk)
        setattr(cls, 'as_choices_vk', as_choices_vk )

        # contains
        has_key = staticmethod(lambda key: key in reverse_name.keys() )
        setattr(cls, 'has_key', has_key )

class MetaEnum(object):
    """
    example of use:

    class FOO(MetaEnum):
        BAZ = (0, 'bazik')
        BAR = 1

    >>> FOO.BAZ
    0
    >>> FOO.BAR
    1
    >>> FOO.BAZ_name
    'BAZ'
    >>> FOO.BAZ_verbose
    'bazik'
    >>> FOO.get_verbose(FOO.BAZ)
    'bazik'
    >>> FOO.get_verbose(FOO.BAR)
    None
    >>> FOO.as_choices()
    [(0, 'bazik'), (1, None)]

    >>> FOO.by_name('BAZ')
    0
    >>> FOO.by_verbose('bazik')
    1
    """
    __metaclass__ = MetaEnumType
