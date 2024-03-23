class VialogosRouter:
    '''
    Router for the Vialogos app
    '''
    def db_for_read(self, model, **hints):
        '''
        Return the database for read
        '''
        if model._meta.app_label == 'vldados':
            return 'vldados'
        return None

    def db_for_write(self, model, **hints):
        '''
        Return the database for write
        '''
        if model._meta.app_label == 'vldados':
            return 'vldados'
        return None

    # def allow_relation(self, obj1, obj2, **hints):
    #     '''
    #     Allow relation between objects
    #     '''
    #     if obj1._meta.app_label == 'vldados' or obj2._meta.app_label == 'vldados':
    #         return True
    #     return None

    # def allow_migrate(self, db, app_label, model_name=None, **hints):
    #     '''
    #     Allow migration
    #     '''
    #     if app_label == 'vldados':
    #         return db == 'vldados'
    #     return None
