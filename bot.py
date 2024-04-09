from dotenv import load_dotenv
import os
from google import generativeai as gen_ai
import pyttsx3
import random
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
from upload import upload
from time import sleep



YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
gen_ai.configure(api_key=GOOGLE_API_KEY)
model=gen_ai.GenerativeModel('gemini-pro')

videos = ["shorts/sample_1.mp4","shorts/sample_2.mp4","shorts/sample_3.mp4"]

prompts = [
    "Echoes of Atlantis: A marine biologist stumbles upon an underwater city that may be the legendary Atlantis, but uncovering its secrets attracts the attention of those who will stop at nothing to keep them hidden.",
    "The Clockwork Circus: A traveling circus comprised of sentient mechanical performers hides a dark secret at its core, and a young acrobat must uncover the truth before it's too late.",
    "The Quantum Thief: In a world where reality is shaped by perception, a master thief must navigate shifting landscapes and rival illusionists to pull off the ultimate heist.",
    "The Song of Stars: A musician discovers that the stars themselves hold a melody that, when played, can unlock the secrets of the universe and alter the course of destiny.",
    "The Alchemist's Apprentice: A young apprentice to a renowned alchemist accidentally unleashes a powerful magical force, setting off a chain of events that could change the world forever.",
    "The Timeless Garden: A mysterious garden exists outside of time, tended by guardians who ensure its flora and fauna remain untouched by the passage of years. But when an outsider discovers its location, the delicate balance is threatened.",
    "The Artisan of Memory: In a society where memories can be bought and sold, a skilled artisan crafts bespoke memories for the elite. But when a client's request leads to a shocking revelation, the artisan must confront the ethics of their trade.",
    "The Celestial Symphony: In the far reaches of space, a cosmic orchestra plays the music of creation itself. But when discord threatens to tear the symphony apart, a group of unlikely heroes must band together to restore harmony to the universe.",
    "Lost in Translation: A linguist discovers an ancient text that could hold the key to understanding a long-lost civilization, but the language proves to be more enigmatic than expected.",
    "The Guardian of Dreams: Every night, a dream guardian must protect the realm of dreams from nightmares that threaten to spill over into the waking world.",
    "The Wizard's Apprentice: A young apprentice to a powerful wizard accidentally releases a malevolent force from an ancient artifact, and must race against time to stop it before it destroys everything.",
    "The Skyship Chronicles: A daring crew embarks on a journey across the skies aboard their magnificent airship, facing perilous adventures and uncovering ancient mysteries along the way.",
    "The Crystal Labyrinth: Deep within a mystical labyrinth lies a legendary crystal said to grant unimaginable power to whoever possesses it. But the labyrinth is filled with traps and illusions, and only the worthy may claim the crystal as their own.",
    "The Clockwork Detective: In a city where magic and technology coexist, a brilliant detective with a mechanical arm solves impossible crimes using a combination of deductive reasoning and cutting-edge gadgets.",
    "The Moonlit Masquerade: At a lavish masquerade ball held under the light of the full moon, hidden identities are revealed and forbidden romances ignite amidst the swirling dances and whispered secrets.",
    "The Forbidden Forest: Deep within an enchanted forest lies a hidden grove where the trees whisper secrets and magical creatures roam free. But trespassers beware, for not all who enter emerge unscathed.",
    "The Starlit Sorcerer: A powerful sorcerer harnesses the energy of the stars to cast spells of unparalleled strength. But when dark forces threaten to extinguish the stars themselves, the sorcerer must embark on a perilous quest to save them.",
    "The Enchanted Marketplace: In a bustling marketplace where magical goods are bought and sold, a humble shopkeeper discovers a mysterious artifact that could change the course of history.",
    "The Crystal Caverns: Deep beneath the earth's surface lie the fabled Crystal Caverns, home to treasures beyond imagination and dangers beyond reckoning. Only the bravest adventurers dare to explore its depths.",
    "The Phoenix's Flight: Legend speaks of a majestic phoenix that rises from the ashes of its own destruction, bringing renewal and hope to a world ravaged by war and despair.",
    "The Astral Explorer: A daring explorer journeys beyond the bounds of reality, traversing the astral plane in search of forgotten knowledge and untold mysteries.",
    "The Clockwork Kingdom: In a kingdom ruled by clockwork automatons, a young inventor discovers the secret to creating life, but soon realizes that some creations are better left unmade.",
    "The Elemental War: The elements themselves rise up in rebellion against humanity, unleashing devastating storms, earthquakes, and wildfires. Only a chosen few with the power to control the elements can restore balance to the world.",
    "The Oracle's Prophecy: A mysterious oracle foretells of a chosen one who will rise to challenge the tyrannical rule of a corrupt king and restore peace to the land.",
    "The Celestial Library: Hidden among the stars lies a vast library containing the knowledge of countless civilizations. But gaining access to its hallowed halls requires solving a series of cryptic riddles and overcoming deadly traps.",
    "The Mechanical Menace: A swarm of self-replicating robots threatens to engulf the world in chaos and destruction. Only a brilliant scientist with a knack for invention can stop them, but time is running out.",
    "The Dragon's Hoard: Deep within a treacherous mountain range lies the lair of a fearsome dragon, hoarding untold riches and guarding them with ferocious intensity. But fortune favors the bold, and a daring band of adventurers sets out to claim the dragon's treasure as their own.",
    "The Wizard's Tower: Perched atop a remote mountain peak stands the tower of a reclusive wizard, rumored to possess arcane knowledge beyond mortal comprehension. But gaining entry to the tower is no easy task, and those who dare to seek its secrets must first overcome a series of perilous trials.",
    "The Feywild: A realm of endless beauty and boundless magic, the Feywild is home to all manner of mystical creatures and enchanting wonders. But those who venture too deep may find themselves lost in its timeless embrace, forever trapped in a world of dreams and illusions.",
    "The Pirate Queen: A swashbuckling pirate captain rules the high seas with an iron fist, plundering merchant ships and evading the law at every turn. But when a rival pirate threatens her reign, she must rally her crew and face them in a battle for supremacy.",
    "The Crystal City: A gleaming city of crystal towers rises from the desert sands, its beauty unmatched by any other in the realm. But beneath its dazzling facade lies a dark secret that could spell doom for all who dwell within its walls.",
    "The Shadow Realm: A realm of darkness and despair, the Shadow Realm is home to unspeakable horrors and malevolent entities. Only the bravest souls dare to venture into its depths, where every shadow hides a new danger.",
    "The Elemental Forge: Deep within the heart of a volcanic mountain lies the Elemental Forge, a legendary forge said to harness the power of the elements themselves. But gaining access to the forge is no easy task, and only those with the strength of will and the courage to face their inner demons can hope to master its secrets.",
    "The Crystal Maze: A labyrinthine maze of crystalline corridors and shifting pathways, the Crystal Maze is said to hold the key to untold riches and unimaginable power. But navigating its treacherous twists and turns requires more than just skill and cunning – it requires unwavering determination and unbreakable resolve.",
    "The Forgotten Kingdom: Once a mighty empire that spanned the known world, the Forgotten Kingdom now lies in ruins, its former glory lost to the mists of time. But legends speak of a prophecy that foretells the kingdom's return, and only those who are worthy can unlock its secrets and restore it to its former greatness.",
    "The Crystal Guardians: Ancient guardians of untold power, the Crystal Guardians watch over the realm from their hidden sanctuaries, protecting it from all who would seek to do it harm. But when a dark force threatens to overthrow the balance of power, the guardians must unite to face their greatest challenge yet.",
    "The Astral Observatory: A celestial observatory hidden among the stars, the Astral Observatory is said to hold the key to unlocking the mysteries of the universe. But gaining access to its hallowed halls requires more than just knowledge – it requires a journey of self-discovery and enlightenment.",
    "The Elemental Warlock: A master of the elements and wielder of untold power, the Elemental Warlock seeks to reshape the world in his image. But when his dark ambitions threaten to plunge the realm into chaos, a group of unlikely heroes must rise up to stop him before it's too late.",
    "The Crystal Guardian: A lone guardian tasked with protecting a powerful crystal from falling into the wrong hands, the Crystal Guardian must fend off hordes of enemies and overcome impossible odds to fulfill his sacred duty.",
    "The Feywild Princess: A princess of the Feywild, blessed with beauty and grace beyond compare, embarks on a quest to reclaim her kingdom from the clutches of a dark sorcerer. But to succeed, she must first learn to harness the full extent of her magical abilities and embrace her destiny as the savior of her people.",
    "The Clockwork Dragon: A fearsome dragon constructed entirely of gears and cogs, the Clockwork Dragon roams the land, leaving destruction in its wake. But when a brave knight dares to challenge it, he discovers that the key to defeating the dragon may lie in its very heart.",
    "The Crystal Sorcerer: A powerful sorcerer who harnesses the power of crystals to cast spells of unparalleled strength, the Crystal Sorcerer seeks to unlock the secrets of the universe and transcend mortal limitations. But in his quest for ultimate power, he risks losing sight of what truly matters most.",
    "The Astral Wanderer: A wanderer who traverses the astral plane in search of adventure and enlightenment, the Astral Wanderer embarks on a journey that takes him to the farthest reaches of the cosmos and beyond.",
    "The Feywild Archer: A skilled archer who hails from the Feywild, the Feywild Archer embarks on a quest to rid the realm of evil and restore balance to the natural order. But to succeed, she must first confront the darkness that lurks within her own heart.",
    "The Clockwork Knight: A knight clad in armor forged from the finest clockwork gears and mechanisms, the Clockwork Knight embarks on a quest to defend the realm from the forces of darkness and restore peace to the land.",
    "The Crystal Mage: A master of crystal magic and wielder of untold power, the Crystal Mage seeks to unlock the secrets of the universe and harness its energies for his own purposes. But in his quest for knowledge, he risks unleashing forces beyond his control.",
    "The Elemental Druid: A druid who draws his power from the elements themselves, the Elemental Druid seeks to protect the natural world from harm and preserve the balance of nature. But when a dark force threatens to destroy everything he holds dear, he must embark on a quest to stop it at any cost.",
    "The Astral Mage: A mage who harnesses the power of the astral plane to cast spells of incredible strength and complexity, the Astral Mage seeks to unlock the secrets of the cosmos and transcend mortal limitations. But in his quest for ultimate knowledge, he risks losing his grip on reality itself.",
    "The Feywild Trickster: A mischievous trickster who hails from the Feywild, the Feywild Trickster delights in playing pranks on unsuspecting travelers and causing chaos wherever he goes. But when his antics attract the attention of a powerful sorcerer, he must use all his wit and cunning to outsmart his foe and escape with his life.",
    "The Clockwork Inventor: An eccentric inventor who creates fantastical machines powered by clockwork gears and mechanisms, the Clockwork Inventor seeks to revolutionize the world with his groundbreaking inventions. But when his latest creation falls into the wrong hands, he must race against time to stop it from being used for nefarious purposes.",
    "The Crystal Enchanter: A master enchanter who imbues crystals with magical properties, the Crystal Enchanter seeks to unlock the full potential of these precious gems and harness their energies for the greater good. But when a rival enchanter threatens to steal his secrets, he must protect his work at all costs.",
    "The Elemental Guardian: A guardian tasked with protecting the elemental planes from outside threats, the Elemental Guardian must use all his strength and cunning to defend the realms of fire, water, earth, and air from those who seek to exploit their power for their own gain.",
    "The Astral Sage: A wise sage who has spent centuries studying the mysteries of the cosmos, the Astral Sage seeks to unlock the secrets of the universe and attain enlightenment. But when a dark force threatens to consume all existence, he must use his knowledge to guide others on the path to salvation.",
    "The Feywild Seer: A seer blessed with the gift of foresight, the Feywild Seer can glimpse the future and unravel the mysteries of fate. But when her visions reveal a terrible prophecy that foretells the end of the world, she must rally her allies and embark on a quest to prevent it from coming to pass.",
    "The Clockwork Guardian: A guardian constructed from the finest clockwork gears and mechanisms, the Clockwork Guardian stands watch over the realm, defending it from all who would seek to do it harm. But when a powerful enemy threatens to overrun the kingdom, he must use all his strength and cunning to protect those under his care.",
    "The Crystal Prophet: A prophet blessed with the ability to commune with the crystals themselves, the Crystal Prophet seeks to unravel the secrets of the universe and share them with the world. But when his teachings attract the attention of a fanatical cult, he must confront them and prevent them from using his knowledge for their own nefarious purposes.",
    "The Elemental Monk: A monk who has mastered the elements themselves, the Elemental Monk seeks to achieve spiritual enlightenment and attain oneness with the universe. But when a dark force threatens to disrupt the balance of nature, he must use his skills to restore harmony to the world.",
    "The Astral Nomad: A nomad who travels the astral plane in search of adventure and enlightenment, the Astral Nomad wanders the cosmos in search of knowledge and wisdom. But when he stumbles upon a hidden conspiracy that threatens the very fabric of reality, he must use all his wits and cunning to uncover the truth and prevent catastrophe.",
    "The Feywild Bard: A bard who draws inspiration from the wonders of the Feywild, the Feywild Bard regales audiences with tales of adventure and romance, weaving magic with his words and music. But when a dark force threatens to engulf the realm in darkness, he must use his talents to rally the people and inspire them to stand against the coming storm.",
    "The Clockwork Tinkerer: A tinkerer who specializes in crafting clockwork contraptions, the Clockwork Tinkerer seeks to push the boundaries of technology and revolutionize the world with his inventions. But when his latest creation goes haywire and threatens to destroy everything in its path, he must race against time to stop it before it's too late.",
    "The Crystal Guardian: A guardian tasked with protecting a powerful crystal from falling into the wrong hands, the Crystal Guardian must fend off hordes of enemies and overcome impossible odds to fulfill his sacred duty.",
    "The Feywild Princess: A princess of the Feywild, blessed with beauty and grace beyond compare, embarks on a quest to reclaim her kingdom from the clutches of a dark sorcerer. But to succeed, she must first learn to harness the full extent of her magical abilities and embrace her destiny as the savior of her people.",
    "The Clockwork Dragon: A fearsome dragon constructed entirely of gears and cogs, the Clockwork Dragon roams the land, leaving destruction in its wake. But when a brave knight dares to challenge it, he discovers that the key to defeating the dragon may lie in its very heart.",
    "The Crystal Sorcerer: A powerful sorcerer who harnesses the power of crystals to cast spells of unparalleled strength, the Crystal Sorcerer seeks to unlock the secrets of the universe and transcend mortal limitations. But in his quest for knowledge, he risks unleashing forces beyond his control.",
    "The Astral Wanderer: A wanderer who traverses the astral plane in search of adventure and enlightenment, the Astral Wanderer embarks on a journey that takes him to the farthest reaches of the cosmos and beyond.",
    "The Feywild Archer: A skilled archer who hails from the Feywild, the Feywild Archer embarks on a quest to rid the realm of evil and restore balance to the natural order. But to succeed, she must first confront the darkness that lurks within her own heart.",
    "The Clockwork Inventor: An eccentric inventor who creates fantastical machines powered by clockwork gears and mechanisms, the Clockwork Inventor seeks to revolutionize the world with his groundbreaking inventions. But when his latest creation falls into the wrong hands, he must race against time to stop it from being used for nefarious purposes.",
    "The Crystal Enchanter: A master enchanter who imbues crystals with magical properties, the Crystal Enchanter seeks to unlock the full potential of these precious gems and harness their energies for the greater good. But when a rival enchanter threatens to steal his secrets, he must protect his work at all costs.",
    "The Elemental Guardian: A guardian tasked with protecting the elemental planes from outside threats, the Elemental Guardian must use all his strength and cunning to defend the realms of fire, water, earth, and air from those who seek to exploit their power for their own gain.",
    "The Astral Sage: A wise sage who has spent centuries studying the mysteries of the cosmos, the Astral Sage seeks to unlock the secrets of the universe and attain enlightenment. But when a dark force threatens to consume all existence, he must use his knowledge to guide others on the path to salvation.",
    "The Feywild Seer: A seer blessed with the gift of foresight, the Feywild Seer can glimpse the future and unravel the mysteries of fate. But when her visions reveal a terrible prophecy that foretells the end of the world, she must rally her allies and embark on a quest to prevent it from coming to pass.",
    "The Clockwork Guardian: A guardian constructed from the finest clockwork gears and mechanisms, the Clockwork Guardian stands watch over the realm, defending it from all who would seek to do it harm. But when a powerful enemy threatens to overrun the kingdom, he must use all his strength and cunning to protect those under his care.",
    "The Crystal Prophet: A prophet blessed with the ability to commune with the crystals themselves, the Crystal Prophet seeks to unravel the secrets of the universe and share them with the world. But when his teachings attract the attention of a fanatical cult, he must confront them and prevent them from using his knowledge for their own nefarious purposes.",
    "The Elemental Monk: A monk who has mastered the elements themselves, the Elemental Monk seeks to achieve spiritual enlightenment and attain oneness with the universe. But when a dark force threatens to disrupt the balance of nature, he must use his skills to restore harmony to the world.",
    "The Astral Nomad: A nomad who travels the astral plane in search of adventure and enlightenment, the Astral Nomad wanders the cosmos in search of knowledge and wisdom. But when he stumbles upon a hidden conspiracy that threatens the very fabric of reality, he must use all his wits and cunning to uncover the truth and prevent catastrophe.",
    "The Feywild Bard: A bard who draws inspiration from the wonders of the Feywild, the Feywild Bard regales audiences with tales of adventure and romance, weaving magic with his words and music. But when a dark force threatens to engulf the realm in darkness, he must use his talents to rally the people and inspire them to stand against the coming storm.",
    "The Clockwork Tinkerer: A tinkerer who specializes in crafting clockwork contraptions, the Clockwork Tinkerer seeks to push the boundaries of technology and revolutionize the world with his inventions. But when his latest creation goes haywire and threatens to destroy everything in its path, he must race against time to stop it before it's too late.",
    "The Crystal Enchanter: A master enchanter who imbues crystals with magical properties, the Crystal Enchanter seeks to unlock the full potential of these precious gems and harness their energies for the greater good. But when a rival enchanter threatens to steal his secrets, he must protect his work at all costs.",
    "The Elemental Guardian: A guardian tasked with protecting the elemental planes from outside threats, the Elemental Guardian must use all his strength and cunning to defend the realms of fire, water, earth, and air from those who seek to exploit their power for their own gain.",
    "The Astral Sage: A wise sage who has spent centuries studying the mysteries of the cosmos, the Astral Sage seeks to unlock the secrets of the universe and attain enlightenment. But when a dark force threatens to consume all existence, he must use his knowledge to guide others on the path to salvation.",
    "The Feywild Seer: A seer blessed with the gift of foresight, the Feywild Seer can glimpse the future and unravel the mysteries of fate. But when her visions reveal a terrible prophecy that foretells the end of the world, she must rally her allies and embark on a quest to prevent it from coming to pass.",
    "The Clockwork Guardian: A guardian constructed from the finest clockwork gears and mechanisms, the Clockwork Guardian stands watch over the realm, defending it from all who would seek to do it harm. But when a powerful enemy threatens to overrun the kingdom, he must use all his strength and cunning to protect those under his care.",
    "The Crystal Prophet: A prophet blessed with the ability to commune with the crystals themselves, the Crystal Prophet seeks to unravel the secrets of the universe and share them with the world. But when his teachings attract the attention of a fanatical cult, he must confront them and prevent them from using his knowledge for their own nefarious purposes.",
    "The Elemental Monk: A monk who has mastered the elements themselves, the Elemental Monk seeks to achieve spiritual enlightenment and attain oneness with the universe. But when a dark force threatens to disrupt the balance of nature, he must use his skills to restore harmony to the world.",
    "The Astral Nomad: A nomad who travels the astral plane in search of adventure and enlightenment, the Astral Nomad wanders the cosmos in search of knowledge and wisdom. But when he stumbles upon a hidden conspiracy that threatens the very fabric of reality, he must use all his wits and cunning to uncover the truth and prevent catastrophe.",
    "The Feywild Bard: A bard who draws inspiration from the wonders of the Feywild, the Feywild Bard regales audiences with tales of adventure and romance, weaving magic with his words and music. But when a dark force threatens to engulf the realm in darkness, he must use his talents to rally the people and inspire them to stand against the coming storm.",
    "The Clockwork Tinkerer: A tinkerer who specializes in crafting clockwork contraptions, the Clockwork Tinkerer seeks to push the boundaries of technology and revolutionize the world with his inventions. But when his latest creation goes haywire and threatens to destroy everything in its path, he must race against time to stop it before it's too late."
]



def get_story():
    try:
        prompt = random.choice(prompts)
        output = model.generate_content(prompt)
        return output.text[:900]
    except ValueError as e:
        return output.text


def get_audio(prompt_title,video):
    mytext = get_story()
    engine = pyttsx3.init()   
    engine.setProperty('rate', 150) 
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) 
    file_name = f"{prompt_title}.mp3"
    engine.save_to_file(mytext, file_name)
    engine.runAndWait()
    video_clip = VideoFileClip(video)
    audio_clip = AudioFileClip(file_name)
    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile(f"{prompt_title}.mp4")


def main():
    for _ in range(3):
        prompt_title = random.choice(prompts).split(":")[0]  
        video = random.choice(videos)
        get_audio(prompt_title, video)
        video_path = f"{prompt_title}.mp4"
        title = prompt_title
        description = f"{prompt_title} #shorts #Story #Adventure #Mystery #random #stories #newworld #askreddit #newask #ask more "
        metadata = {
            "title": title,
            "description": description,
            "tags": ["shorts","random","stories","new","askreddit","stories","randomstoires"]
    }
        # if upload(video_path,metadata):
      
        #     # os.remove(video_path)
        #     os.remove(f"{prompt_title}.mp3")
        # else:
        #     print("Failed to upload video. Video file will not be deleted.")
        # sleep(18000)
        os.remove(f"{prompt_title}.mp3")
        sleep(5)



if __name__ == "__main__":
    main()