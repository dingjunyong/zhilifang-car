# -*- coding: utf-8 -*-
import datetime
from application.extensions import db, bcrypt
from flask_login import UserMixin

from configs.enum import USER_ROLE
from configs import signals

__all__ = ['Shop','ShopMember']


class ShopMember(db.Model):
    __tablename__ = 'shop_members'
    id = db.Column(db.Integer, primary_key=True)
    mobile_number = db.Column(db.String(100))
    is_manager= db.Column(db.Boolean,default=False)

    shop_id = db.Column(db.Integer, db.ForeignKey('shops.id'))
    shop = db.relationship("Shop", back_populates="members")

    @classmethod
    def create(cls, mobile_number, is_manager,shop_id):
        shop_member = ShopMember(mobile_number=mobile_number,
                                 is_manager=is_manager,
                                 shop_id=shop_id)
        db.session.add(shop_member)
        db.session.commit()
        return shop_member




class Shop(db.Model):
    __tablename__ = 'shops'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    img = db.Column(db.String(255))
    telephone1 = db.Column(db.String(100))
    telephone2 = db.Column(db.String(100))
    state = db.Column(db.String(100))
    city = db.Column(db.String(100))
    street = db.Column(db.String(255))
    free_times = db.Column(db.Integer, default=2)
    use_description = db.Column(db.String(100), default=2)
    shop_description = db.Column(db.Text)
    statu = db.Column(db.Integer, default=0)
    is_deleted = db.Column(db.Boolean,default=False)
    deleted_date = db.Column(db.DateTime)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    members = db.relationship("ShopMember", back_populates="shop")

    @classmethod
    def create(cls, name):
        shop = Shop(name=name)
        db.session.add(shop)
        db.session.commit()
        return shop

    @classmethod
    def mark_deleted(cls):
        if cls.is_deleted:
            return
        cls.is_deleted = True
        cls.deleted_date = datetime.datetime.utcnow()
        db.session.commit()