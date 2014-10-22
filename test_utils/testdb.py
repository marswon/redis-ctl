import redisctl.db
import testconf

DB_CONF = testconf.TEST_CONF['mysql']


def reset_db():
    redisctl.db.Connection.init(**DB_CONF)
    with redisctl.db.update() as client:
        client.execute('''DELETE FROM `cache_instance` WHERE 0=0''')
        client.execute('''DELETE FROM `application` WHERE 0=0''')
