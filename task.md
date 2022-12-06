Lets we have a django project.
With models:

Rental

- name

Reservation

- rental_id
- checkin(date)
- checkout(date)

Add the view with the table of Reservations with "previous reservation ID".

Previous reservation is a reservation that is before the current one into samerental.

_Example:_

**Rental-1**
Res-1(2022-01-01, 2022-01-13)
Res-2(2022-01-20, 2022-02-10)
Res-3(2022-02-20, 2022-03-10)

**Rental-2**
Res-4(2022-01-02, 2022-01-20)
Res-5(2022-01-20, 2022-02-11)

<img width="861" alt="image" src="https://user-images.githubusercontent.com/115542336/205841072-8d3844ea-e0ab-4841-b222-187b87b7f99a.png">

Also, add a tests.

Create it into github repo and provide a link to it.
