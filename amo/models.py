from django.db import models

class ManagerBase(models.Manager):
    """
    Base for all managers in AMO.
    Returns BaseQuerySets.
    If a model has translated fields, they'll be attached through a transform
    function.
    """

    pass

class SearchMixin(object):

    ES_ALIAS_KEY = 'default'
    """
    @classmethod
    def _get_index(cls):
        indexes = settings.ES_INDEXES
        return indexes.get(cls.ES_ALIAS_KEY)

    @classmethod
    def index(cls, document, id=None, refresh=False, index=None):
        search.get_es().index(
            body=document, index=index or cls._get_index(),
            doc_type=cls.get_mapping_type(), id=id, refresh=refresh)

    @classmethod
    def unindex(cls, id, index=None):
        id = str(id)
        es = search.get_es()
        try:
            es.delete(index or cls._get_index(), cls._meta.db_table, id)
        except elasticsearch.TransportError:
            # Item wasn't found, whatevs.
            pass

    @classmethod
    def search(cls, index=None):
        return search.ES(cls, index or cls._get_index())

    @classmethod
    def get_mapping_type(cls):
        return cls._meta.db_table
    """

class SaveUpdateMixin(object):
    
    def reload(self):
        """Reloads the instance from the database."""
        from_db = self.__class__.get_unfiltered_manager().get(pk=self.pk)
        for field in self.__class__._meta.fields:
            try:
                setattr(self, field.name, getattr(from_db, field.name))
            except models.ObjectDoesNotExist:
                # reload() can be called before cleaning up an object of stale
                # related fields, when we do soft-deletion for instance. Avoid
                # failing because of that.
                pass
        return self
    """
    @classmethod
    def get_unfiltered_manager(cls):
        return getattr(cls, 'unfiltered', cls.objects)  # Fallback on objects.

    def update(self, **kw):
        signal = kw.pop('_signal', True)
        cls = self.__class__
        for k, v in kw.items():
            setattr(self, k, v)
        if signal:
            # Detect any attribute changes during pre_save and add those to the
            # update kwargs.
            attrs = dict(self.__dict__)
            models.signals.pre_save.send(sender=cls, instance=self)
            for k, v in self.__dict__.items():
                if attrs[k] != v:
                    kw[k] = v
                    setattr(self, k, v)
        # We want this to not fail mysteriously for filtered out objects (eg
        # deleted or unlisted).
        objects = cls.get_unfiltered_manager()
        objects.filter(pk=self.pk).update(**kw)
        if signal:
            models.signals.post_save.send(sender=cls, instance=self,
                                          created=False)

    def save(self, **kwargs):
        # Unfortunately we have to save our translations before we call `save`
        # since Django verifies m2n relations with unsaved parent relations
        # and throws an error.
        # https://docs.djangoproject.com/en/1.9/topics/db/examples/one_to_one/
        if hasattr(self._meta, 'translated_fields'):
            save_translations(id(self))
        return super(SaveUpdateMixin, self).save(**kwargs)
    """

class ModelBase(SearchMixin, SaveUpdateMixin, models.Model):
    """
    Base class for AMO models to abstract some common features.
    * Adds automatic created and modified fields to the model.
    * Fetches all translations in one subsequent query during initialization.
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = ManagerBase()

    class Meta:
        abstract = True
        get_latest_by = 'created'
        # This is important: Setting this to `objects` makes sure
        # that Django is using the manager set as `objects` on this
        # instance reather than the `_default_manager` or even
        # `_base_manager` that are by default configured by Django.
        # That's the only way currently to reliably tell Django to resolve
        # translation objects / call transformers.
        # This also ensures we don't ignore soft-deleted items when traversing
        # relations, if they are hidden by the objects manager, like we
        # do with `addons.models:Addon`
        base_manager_name = 'objects'
    """
    def get_absolute_url(self, *args, **kwargs):
        pass
    
    def serializable_reference(self):
        pass
    """