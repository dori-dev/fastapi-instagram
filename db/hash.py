from passlib.context import CryptContext


class Hash:
    pwd_cxt = CryptContext(schemes='bcrypt', deprecated='auto')

    @classmethod
    def bcrypt(cls, password):
        return cls.pwd_cxt.hash(password)

    @classmethod
    def verify(cls, plain_password, hashed_password):
        try:
            return cls.pwd_cxt.verify(plain_password, hashed_password)
        except Exception:
            return False
