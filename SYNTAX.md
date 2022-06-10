# Syntax Sheet

> This paper is _not_ a tutorial. It is purely for me as a developer, as a way to have a little notebook to store all the syntax I used in this project. Feel free to reference it as a quick cheatsheet though.

## Data declaration

In Veri, data does not only consist of the actual data, but also of some metadata. To be exact, every data declaration in Veri consists of the actual data, a data type, the creation date and the last accession date. A sample data would be stored as such:

```
dec dataname: (
    type: str;;
    data: "Hello World!";;
    creation: 1643712767;;
    last: 1652445287;;
)
```

As can be seen, every data declarion starts with the keyword `dec`. A type has to be declared, which will be listed in a future part, the data comes along, then the creation date followed by the last accession date. The order of these are not important but all of them has to be existing.

## Data types

In Veri, there are x data types. These are:

- String: Declared by keyword 'str', it declares a text string. A string data has to be surrounded by quotations.
- Array: Declared by keyword 'arr', it declares an array, which is an ordered list of same-type items. An array also takes an additional argument to define its content's type, as `arrtype: str`.
- Integer: An integer is a number without decimal points, defined by 'int'.
- Float: A float is a number with decimal points, and is defined by 'flt'.
- Time: Time stores given time in Unix Epoch. The data is stored as Unix Epoch, and has to be inputted as such too. It returns a floating point number, which would be the Unix Epoch that was saved. It is defined as 'tme'.
- Collection: A collection is an array that consists of other declarations. It will be covered in a future section. It is defined as 'col'.

## Arrays

In Veri, an array is a group of items of the same type that are in a numbered list. An example of an array is as such:

```
dec array: (
    type: arr;;
    arrtype: str;;
    creation: 1643712767;;
    last: 1652445287;;
    data: (
        -1- "Foo"
        -2- "Bar"
        -3- "Hello World"
    );;
)
```

## Collections

In Veri, a collection is an array that consists of other declarations. It basically is a way to nest definitions of multiple types. The nested items in a collection must still have a `type` and `data` (and `arrtype` in the case of an array), but the nested items must **not** have timestamps, every action done will count on the timestamp of the parent element. An example collection with multiple entries is as such:

```
dec collection: (
    type: col;;
    creation: 1643712767;;
    last: 1652445287;;
    data: (
        -1- (
            type: str;;
            data: "Foo";;
        )
        -2- (
            type: int;;
            data: 42;;
        )
        -3- (
            type: flt;;
            data: 420.69;;
        )
        -4- (
            type: tme;;
            data: 1643712767.21432;;
        )
        -5- (
            type: arr;;
            arrtype: str;;
            data: (
                -1- "Foo"
                -2- "Bar"
                -3- "Hello World"
            );;
        )
    );;
)
```

