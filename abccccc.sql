INSERT INTO core_polity (id, end_year, name) VALUES (1, 1795, 'CnQingE');
INSERT INTO core_polity (id, start_year, name) VALUES (2, 1795, 'CnQingL');

BEGIN 
    FOR temprow IN SELECT * FROM crisisdb_agricultural_population 
    LOOP
        INSERT INTO crisisdb_agricultural_population_citations (agricultural_population_id,citation_id) VALUES(temprow.id,'9b18b8d4-6682-4a4d-9250-6dd38e165d86');
    END LOOP;
END;

INSERT INTO crisisdb_agricultural_population_citations (agricultural_population_id,citation_id)
SELECT old_seasonnum,player_idd,season_ptss FROM crisisdb_agricultural_population


INSERT INTO crisisdb_agricultural_population_citations (agricultural_population_id,citation_id) VALUES(2,'9b18b8d4-6682-4a4d-9250-6dd38e165d86');

SELECT * FROM crisisdb_agricultural_population;