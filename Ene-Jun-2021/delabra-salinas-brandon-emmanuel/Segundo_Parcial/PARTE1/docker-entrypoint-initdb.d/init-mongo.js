db.createUser({
    user: 'foo',
    pwd: 'bar123',
    roles: [
      {
        role: 'dbOwner',
        db: 'baz',
      },
    ],
  });