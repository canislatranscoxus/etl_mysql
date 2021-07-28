Insert into stg_mty_metro_area

select min(d_codigo) min_cp, max(d_codigo) max_cp, D_mnpio #, d_ciudad, d_asenta 
from ship_cp
where D_mnpio in (
'apodaca',
#'cadereyta jimenez',
'escobedo',
'garcia',
'guadalupe',
'juarez',
'monterrey',
#'salinas victoria',
'san nicolas de los garza',
'san pedro garza garcia',
'santa catarina'
#'santiago'
)
group by D_mnpio 
order by 1
;
