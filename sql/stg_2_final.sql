insert into ship_mty_metro_area 	

    select row_number() over(), min_cp, max_cp, D_mnpio 
    from stg_mty_metro_area;
   