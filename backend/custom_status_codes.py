from backend.constants import KEY_ERR_CODE, KEY_MESSAGE, KEY_SUCCESS_CODE

USERS_SIGN_UP_FAILURE = {
    KEY_ERR_CODE: '1000',
    KEY_MESSAGE: 'Error ! while signing you up.'
}
USER_ACCOUNT_ALREADY_EXISTS = {
    KEY_ERR_CODE: '1001',
    KEY_MESSAGE: 'Oh No ! Email  already exists.'
}
USERS_SIGN_UP_SUCCESS = {
    KEY_SUCCESS_CODE: '2000',
    KEY_MESSAGE: 'Your account is created successfully.'
}
USERS_SIGN_IN_FAILURE = {
    KEY_ERR_CODE: '1002',
    KEY_MESSAGE: 'There was an error while logging you in'
}
USERS_SIGN_IN_SUCCESS = {
    KEY_SUCCESS_CODE: '2001',
    KEY_MESSAGE: 'You are logged in successfully'
}
ADD_ITEMS_FAILURE = {
    KEY_ERR_CODE: '1003',
    KEY_MESSAGE: 'There was an error while inserting the record'
}
AUTHORIZATION_FAILURE = {
    KEY_ERR_CODE: '1004',
    KEY_MESSAGE: 'You are not authorized to access this.'
}
ADD_ITEMS_SUCCESS = {
    KEY_SUCCESS_CODE: '2002',
    KEY_MESSAGE: 'Your record was inserted'
}
UPDATE_ITEM_SUCCESS = {
    KEY_SUCCESS_CODE: '2004',
    KEY_MESSAGE: 'Record was updated successfully!'

}

UPDATE_ITEM_FAILURE = {
    KEY_ERR_CODE: '1006',
    KEY_MESSAGE: 'There was an error while updating record'
}
VIEW_ITEM_SUCCESS = {
    KEY_SUCCESS_CODE: '2003',
    KEY_MESSAGE: 'Item displayed'
}
VIEW_ITEM_FAILURE = {
    KEY_ERR_CODE: '1005',
    KEY_MESSAGE: 'There was an error while displaying data.Please check again.'
}
LIST_ITEMS_FAILURE = {
    KEY_ERR_CODE: '1007',
    KEY_MESSAGE: 'There was an error while listing the data.'
}
LIST_ITEMS_SUCCESS = {
    KEY_SUCCESS_CODE: '2005',
    KEY_MESSAGE: 'Items listed successfully.'
}
ORDER_PLACED_SUCCESS = {
    KEY_SUCCESS_CODE: '2006',
    KEY_MESSAGE: 'Your order is placed successfully'
}
ORDER_PLACED_ERROR = {
    KEY_ERR_CODE: '1008',
    KEY_MESSAGE: 'There was a problem while placing your order'
}
NO_ITEM_ERROR = {
    KEY_ERR_CODE: '1009',
    KEY_MESSAGE: 'There are no items in your cart.'
}
ID_IMPROPER = {
    KEY_ERR_CODE: '1010',
    KEY_MESSAGE: 'ID INVALID'
}
DELETE_ITEMS_SUCCESS= {
    KEY_SUCCESS_CODE : '2007',
    KEY_MESSAGE : 'Item deleted successfully.'
}