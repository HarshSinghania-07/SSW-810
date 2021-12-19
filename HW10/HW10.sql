---- SSW 810 - HW 10 ----
select Gender, count(*) as G_count from patient where Gender = "M";

select * from doctor where Speciality = "Cardiologists";

select * from patient order by First_Name asc;

select Speciality, count(*) as S_count from doctor group by Speciality;

select p.first_name, p.last_name, p.id, p.date_of_birth, p.gender from patient p join doctor d on d.Patient_ID = p.ID;
