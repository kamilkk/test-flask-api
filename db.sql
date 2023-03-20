create table if not exists public.device
(
    id          integer     not null constraint device_pk primary key,
    location_id uuid        not null
);

create table if not exists public.temperature
(
    id          integer             not null constraint temperature_pk primary key,
    device_id   integer             not null constraint temperature_device_id_fk references public.device,
    timestamp   integer             not null,
    value       double precision    not null
);

create unique index if not exists temperature_timestamp_uindex on public.temperature (timestamp);

