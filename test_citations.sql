/*BEGIN
FOR temprow IN SELECT * FROM crisisdb_agricultural_population
LOOP
    INSERT INTO crisisdb_agricultural_population_citations (agricultural_population_id,citation_id) VALUES (temprow.id,'9b18b8d4-6682-4a4d-9250-6dd38e165d86');
    raise notice 'Value: %', temprow.id;
END LOOP;
END
*/

INSERT INTO crisisdb_agricultural_population_citations (agricultural_population_id,citation_id) VALUES(1,'9b18b8d4-6682-4a4d-9250-6dd38e165d86');
INSERT INTO crisisdb_agricultural_population_citations (agricultural_population_id,citation_id) VALUES(2,'9b18b8d4-6682-4a4d-9250-6dd38e165d86');
INSERT INTO crisisdb_agricultural_population_citations (agricultural_population_id,citation_id) VALUES(3,'9b18b8d4-6682-4a4d-9250-6dd38e165d86');
INSERT INTO crisisdb_agricultural_population_citations (agricultural_population_id,citation_id) VALUES(4,'9b18b8d4-6682-4a4d-9250-6dd38e165d86');
INSERT INTO crisisdb_agricultural_population_citations (agricultural_population_id,citation_id) VALUES(5,'9b18b8d4-6682-4a4d-9250-6dd38e165d86');
