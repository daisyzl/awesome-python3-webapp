import asyncio

from www import orm
from www.models import User


async def test(loop):
    await orm.create_pool(loop,host='127.0.0.1', port=3306, user='root', password='123',db='awesome')
    u = User(name='Test1', email='test1@example.com', passwd='1234567890', image='about:blank')
    print("dsdasdsa")
    await u.save()

async def find(loop):
    await orm.create_pool(loop,user='www-data',password='www-data',db='awesome')
    rs = await User.findAll()
    print("hlh")
    print('查找测试： %s' % rs)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([test(loop),find(loop)]))
loop.run_forever()