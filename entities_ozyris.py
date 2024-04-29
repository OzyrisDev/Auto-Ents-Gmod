

#   → This code is proprietary of Ozyris(698678018159411280) © 2024 
#    → Developer : 'Ozyris(698678018159411280)
#   → All rights reserved.



import os


def create_entity_files(entity_path, print_name, category): # Le INIT DE TON ENTITER BEBOU
    init_lua_content = '''
--==============================--
-- By Ozyris					--
-- Discord: user29262		--
--==============================--
AddCSLuaFile("cl_init.lua")
AddCSLuaFile("shared.lua")
include("shared.lua")

timer_Simple = timer.Simple

function ENT:Initialize()
    self:SetModel( "models/hunter/blocks/cube025x025x025.mdl" )
	self:PhysicsInit( SOLID_VPHYSICS )      
	self:SetMoveType( MOVETYPE_VPHYSICS )   
	self:SetSolid( SOLID_VPHYSICS )         
	local phys = self:GetPhysicsObject()
	if (phys:IsValid()) then
		phys:Wake()
	end
	SafeRemoveEntityDelayed(self, 5)
end

function ENT:Touch(v)
	if v:IsPlayer() or v:IsNPC() or v:IsNextBot() then 
		v:TakeDamage(150, ply, ply)
	end 
end 


function ENT:PhysicsCollide(data, phys)
	self:Remove()
end

'''
     # Le CL DE TON ENTITER BEBOU
    cl_init_lua_content = '''  
    --==============================--
-- By Ozyris					--
-- Discord: user29262		--
--==============================--

include("shared.lua") 
AddCSLuaFile() 

function ENT:Draw()
    self:DrawModel()
end
'''
         # Le SHARED DE TON ENTITER BEBOU

    shared_lua_content = f'''
--==============================--
-- By Ozyris					--
-- Discord: user29262		--
--==============================--

AddCSLuaFile()

ENT.Type = "anim"
ENT.Base = "base_gmodentity"
ENT.PrintName = "{print_name}"
ENT.Category = "{category}"
ENT.Author = "Ozyris"
ENT.Spawnable = true
ENT.AdminOnly = false

'''
      # PAS TOUCHE A CA
    with open(os.path.join(entity_path, 'init.lua'), 'w') as f:
        f.write(init_lua_content)
        
    with open(os.path.join(entity_path, 'cl_init.lua'), 'w') as f:
        f.write(cl_init_lua_content)
        
    with open(os.path.join(entity_path, 'shared.lua'), 'w') as f:
        f.write(shared_lua_content)

def create_entity():          # PAS TOUCHE A CA

    entity_name = input("Please enter the name of the entity: ")
    print_name = input("Please enter the name to be displayed in-game: ")
    category = input("Please enter the entity category: ")
    entity_path = input("Please enter the path where to create the entity: ")
    
    entity_folder_path = os.path.join(entity_path, entity_name)
    os.makedirs(entity_folder_path, exist_ok=True)
    
    create_entity_files(entity_folder_path, print_name, category)
    print(f"Entity '{entity_name}' successfully created in folder '{entity_folder_path}'.'.")

if __name__ == "__main__":
    create_entity()
