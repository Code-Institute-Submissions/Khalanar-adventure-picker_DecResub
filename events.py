import sys
import os
from gamemanager import *

# Declare player object
player = Player(3, "sword", 100)

# Declare all enemy types
rat = Enemy("rat", 5, 2)
necromancer = Enemy("necromancer", 10, 3)
boar = Enemy("boar", 6, 3)

# Declare all combat events
rat_combat = Combat(rat, player)
necromancer_combat = Combat(necromancer, player)
boar_combat = Combat(boar, player)

# Declare all events as empty so they can be referenced no
# matter when they have their values assigned
game_start = Event()  #
check_wallet = Event()  #
unsheathe_sword = Event()  #
approach_bush = Event()  #
dead_rat = Event()  #
run_from_bushes = Event()  #
reach_town = Event()  #
go_to_river = Event()  #
wounded_boar = Event()  #
heal_boar = Event()  #
lay_hands = Event()  #
stand_up = Event()  #
inspect_corpse = Event()  #
carry_corpse = Event()  #
agree_necro = Event()  #
disagree_necro = Event()  #
approach_lamias = Event()  #
attack_lamias = Event()  #
help_execution = Event()  #
steal_crowd = Event()  #

# Special Game Over events
approach_bushes_gameover = Event()  #
trust_gut_gameover = Event()  #
restart_game = Event()

game_start.create_event(
    "You wake up in the middle of a forest. You are not sure where you are. Judging by the amount of moss in the trees around you, somewhere in the middle of Spring in the northern hemisphere. You have no memories whatsoever of ever having come to this forest, and something about it unsettles your stomach\nYour trusty sword is firmly sheathed, which is a good sign, you have not been robbed. Or so you think.",
    [["Check coin purse", check_wallet],
     ["unsheathe sword", unsheathe_sword]])

check_wallet.create_event(
    f"You reach out to your coin purse but it's not in your belt. At least nowhere to be found. You start to panic but realize you're wearing it to the right of your belt instead of the left. Odd, you have always worn it in your left side. There's {player.gold} coins in it. You don't remember how much you had left, or when was the last time you actually used it.",
    [["unsheathe sword", unsheathe_sword],
     ["Stand up", stand_up]])

unsheathe_sword.create_event(
    "You reach out to your sword but can't unsheathe it. It feels stuck. Upon closer inspection you realise it's not all the way in. You pull harder and manage to unsheathe your steel, completely covered in dried-out blood so thick that you think it might have been responsible for ruining your prime-leather scabbard. While you lament the moment you ever put your sword away before cleaning it, the bushes to your left start rustling.",
    [["Check bushes", approach_bush],
     ["run", run_from_bushes]])

approach_bush.create_event(
    "Your brain tells you your sword will be practically useless in this state but your heart is pumping with anticipation. As you approach the bushes, a rat comes out. It's not a normal rat. There is something vicious about the way it looks at you. Like an animal without any self-preservation instincts, like an animal taken away by something dark that you can't begin to comprehend.",
    [["Attack", dead_rat, rat_combat],
     ["run", run_from_bushes]])

dead_rat.create_event(
    "The rat lies dead. Its severed body now covered in blood and soil emits a hissing sound while thick blood comes out from the hole where the head used to be. You feel a strange urge to carry the animal's remains but at the same time it does not seem like a good idea. You are disgusted and at the same time attracted to the creature's oozing blood.",
    [["inspect corpse", inspect_corpse],
     ["carry corpse", carry_corpse]])

run_from_bushes.create_event(
    "You feel something big is lurking behind the bushes. You can't explain what it is but it is certainly something bigger than the rat that from the bushes jumps at you. Something bigger in power, can it be controlling the frenzied animal? There is no time to think, your run.\n\nYou run as fast as you can for as long as you can. You run for so long that you forget what you were running from. Running itself becomes the objective in your mind, running itself and not escaping from that of which you are running from. This does not make much sense but you completely forgot what you were running from, only a deep sense of dread lingers in your heart.\n\nExhausted you reach a small lake and you can see some smoke coming off the other side of the lake, behind the trees. A town, and the bridge to cross to the other side is mere meters away! You thought of sleeping in a hay bed again warms your heart, but you are thirsty and kneel down at the shore to refill your water pelt.\n\nAs you kneel down you see a boar. A regular wild boar if it were not for its incredible size and white fur. It's looking at you, menacingly, as it scratches the soil with its hoof readying to charge.",
    [["Attack", wounded_boar, boar_combat],
     ["Run to bridge", reach_town]])

wounded_boar.create_event(
    "There is a spark of life left in the animal. You feel sorry for the poor thing and don't believe the attack was ill-intentioned, it was protecting its territory and you chose violence instead of de-escalating by slowly moving away. What came over you? You have some spare nuts which you can use to feed the boar and some bandages to heal the boar, but like a person who has received a calling from above, you start to feel a strange energy flowing through",
    [["Heal boar", heal_boar],
     ["Lay hands on boar", lay_hands]])

heal_boar.create_event(
    "You sense a deep connection to this animal and regret the minute you lay hands on her. 'Her?' you say. You never checked yet you know this animal is a female. You apply some ointment in the animal's wounds and feed her some dried fruits you were carrying. While caressing her mane you speak words of forgiveness and stay with her in her last moments. A few minutes later, the animal stands back up and presses her body against yours, right before, like a well-trained dog, sits on her two back legs. You immediately understand what is going on.\n\n\nThis path will eventually lead you to becoming a Forest Guardian.\n\nChapter 2 coming soon:",
    [["Restart", game_start],
    ["Exit", sys.exit]])

lay_hands.create_event(
    "Posessed by something you can't yet comprehend, you lay your hands on the animal's head and open your mouth. You feel your head starts vibrating in a low frequency that starts to pick up as it echoes in the boar's body through your hands. With your mouth still wide open some words come from it. You never pronouned those words, you don't know those words and they don't sound like any language you have ever heard before. The now high-pitched rining suddenly stops and the boar gets up and starts running to the woods as if it was completely overwhelmed by what just happened.\n\n\nThis path will eventually lead you to becoming a Speaker of Anuk.\n\nChapter 2 coming soon:",
    [["Restart", game_start],
    ["Exit", sys.exit]])

reach_town.create_event(
    "You start running towards the bridge. You know walking back slowly would have been the better option, non-verbally telling the boar that you wished it no harm. But you chose to run. Stupid, you feel stupid and look back at other impulse-driven life choices that brought you here today. Before you realise you're already at the city's doors. 'Welcome to Howthsand' reads a sign atop of a heavy-barred gate that's thankfully open.\n\nAs you walk into the city you find dozens of townfolk gathered around the gallows where the face-covered executioner is trying to take hold of an escaped prisoner, who mockingly dodges the executioners axe blows while open-handedly slapping him in the belly, to the crowd's content. You feel pity for the executioner who is just trying to do his job, albeit being terribly bad at it, but can also see why the townsfolk are enjoying the moment, laughing at the sad display of this executioner",
    [["Stop the show", help_execution],
     ["Steal", steal_crowd]])

stand_up.create_event(
    "You stand up, you feel dizzy. You're unsure if for the lack of food or lack of sleep, but it's certainly a feeling you are not used to. Before you can even make sense to whatever is going on with you, your gut rumbles, there is something odd about the bushes next to you.",
    [["Approach",approach_bushes_gameover],
    ["unsheathe sword", unsheathe_sword]])

inspect_corpse.create_event(
    "You get closer to the rat's dead body. The rate at which the blood comes out of is down to a trickle and its slightly sweet arome fills the air. It's a strangely comforting smell however repulsive the image before you may be. You can't take this anymore, clean your sword against your pantalons and continue down a trail near you. Eventually you can the running waters of a stream. Judging by the pitch of the water moving through the rocks you can tell it's cold. Colder than what the biome in the area may suggest. This may be ice water trickling down from a nearby mountain. If there's snowpure water, there must be a town somewhere along the stream so you decide to follow it.\n\nAfter some hours down-stream, you can hear chanting. Beautiful chanting. After getting closer you realise these aren't human voices, it's lamias. These half-fish creatures are known to roam from town to town, stealing kids off their homes and devouring them. These are not figments of an overly cautious society telling tales to avoid their little ones to stray too far away. Lamias are real, and four of them are right in front of you, unsuspecting.",
    [["Approach Lamias", approach_lamias],
     ["Attack Lamias", attack_lamias]])

carry_corpse.create_event(
    "The thought of carrying this dead rat repulses you but at the same time you feel it's the right thing to do. You have to fight against your insticts to be able to even touch it. You grab the rat and shove it into your coin purse. You gag as you pull your hand from the purse. Why are you even doing this? It's almost as there is a second voice in your head pulling you into doing this. You are so disgusted by all this that thread closed the coin sack and continue down the small pathway.\n\nIt's getting dark and cold. The still warm cadaver is the only source of heat you have right now. As you think about making camp, you see a strange greenish light. You don't want to get closer but you haven't eaten in a day and the smell of cinnamon rolls draws you to the source.\n\nYou see an old man in dark robes with silver threading. As you accept the old man's request he starts talking to you about a source of immeasurable power. By the way he speaks you can't avoid but thinking that all your recent actions have been in some way influenced by this man and the power he speaks of. Can this even be? You think you're going crazy.\n\nThe old man suggests you join him, in his quest for power in his quest for power there's space for a young apprentice.",
    [["Accept", agree_necro],
     ["Attack", disagree_necro, necromancer_combat]])

agree_necro.create_event(
    "The idea of close to infinite power sounds far too good to be true, but something in the eyes of this old man suggest excitedly he is not lying. He realises you are not totally conviced. With a flick of his fingers and a deep, gutural hum, his eyes start emitting a green color. Green as the fire that brought you here in the first place but you just realise that the fire keeping you both warm is a normal fire. A smokey light emitting substance starts flowing up to the sky from the old man's eyes. Soon all his body is covered and the light becomes so intense you can't lay your eyes directly on him. With a quick click of fingers, all the smoke disappears. The old man gently blows air in your general direction. 'My god's will is stronger than death, apprentice' he utters, as the rat starts scratching your coin purse from inside it.\n\n\nThis path will eventually lead you to becoming a Servant of the God of Life.\n\nChapter 2 coming soon:",
    [["Restart", game_start],
    ["Exit", sys.exit]])

disagree_necro.create_event(
    "The Necromancer lies dead with a smile in its face. You can feel how your thoughts belong to you again. This decrepit old man was a puppeteer playing the strings of a game you can't even start to comprehend, however you are certain you made the right decision. There is no place in this world for the wretchedness of black majiks.\n\nYour sword starts glowing as you lift it to the air. Is this one of the Minor God's doing? The light intensifies as it starts flowing to your wounds, healing them. You can't give credit to what you are experiencing. As a warrior that has taken an oath to a king he has never met, you feel bound by duty to a God you aren't even sure it exists.\n\nAs you sheath your still glowing sword you hear a whisper 'Terzahl'. You speak 'Is that your name, my lord of light?' but no one answers.\n\n\nThis path will eventually lead you to becoming a Servant of the Sun God.\n\nChapter 2 coming soon:",
    [["Restart", game_start],
    ["Exit", sys.exit]])

approach_lamias.create_event(
    "Attracted by their singing you walk towards the demons. The four Lamias sense your presence, turn around and stop singing. They put their hands to their sides with their palms facing you, in a gesture of non-aggression. These rogue Lamias left their old ways many years ago. They became aware of the amount of suffering they were inflicting and decided to stop hunting human babies in exchange for eternal life. Their human half, which has always been the epitome of beauty and youth, start to show the signs of the passing of time. Wrinkles and a couple of white hairs testify to the truth of their story. You can't help but feel in losing their everlasting youth they have acquired something even more precious, humanity. They offer you the chance to adventure with them, they want to learn more about those humans they hunted for centuries. In exchange they will teach you their craft of their singing.\n\n\nThis path will eventually lead you to becoming a Bard.\n\nChapter 2 coming soon:",
    [["Restart", game_start],
    ["Exit", sys.exit]])

attack_lamias.create_event(
    "As you unsheathe your sword the four demons stop singing. You bland your sword with such swiftness that the air around it whistles excitedly. You slash so quickly through one of the demons neck, that before the beheaded body touches the ground your blade is already handle deep into another one's chest stopping her heart immediately. The third Lamia opens her mouth in an act you interpret as singing. If she starts singing you may be drawn into doing things you don't want to. These is how these demons mind-control their victims. Before she can mutter a word, you slide your sword into her mouth. With her eyes fixed to you, you start to feel shame for her as she starts gargling blood. Not 'her', 'it' you think to yourself as you pull the sword back from her and pull the corpse to a side in the same motion.\n\nThe fourth Lamia drops to her knees with her hands to the ground and speaks 'we are sorry'. This fills you with an uncontrollable rage as you remember the smell of fish and the  the trail one of these disgusting creatures next to your baby sister's crib some odd 10 years ago. You raise your sword with both hands over your head and a scream of rage accompanies your slash towards the creature's head. Right before the blade strikes the Lamia speaks again, 'thank you'.\n\n\nThis path will eventually lead you to becoming a Demon Slayer.\n\nChapter 2 coming soon:",
    [["Restart", game_start],
    ["Exit", sys.exit]])

help_execution.create_event(
    "Public executions are not a joke. Maintaining law and order is not a joke. Enforcing the laws of men as handed down by the Gods is not a joke. 'ENOUGH' you scream as you make your way towards the gallows through the cheerful mass. You unsheathe the sword as you climb the stairs and without even looking at the prisoner you slice his whole arm off and pierce through the executioners heart in the same strike.\n\nThe crowd goes silent and looks at you while you wipe off the blood on your sword in your forearm.\n\n\nThis path will eventually lead you to becoming the Emperor's Sword.\n\nChapter 2 coming soon:",
    [["Restart", game_start],
    ["Exit", sys.exit]])

steal_crowd.create_event(
    f"This is a perfect opportunity if you have ever seen one. You reach to your coin pouch and weigh it in your left hand. There's no way {player.gold} coins will pay for your night here, let alone some food and enough mead to help you pass out until morning. You start reaching into people's pockets and steal to your heart's content. Life is easy if you take on the opportunities that are presented to you, you think while you imagine the absurd amount of mead you are going to drink tonight, to the health of the townsfolk of Howthsand. Heck you might even spare a couple coins in the town chapel to help the poor. You may be a thief but you're not heartless.\n\n\nThis path will eventually lead you to becoming a Thief.\n\nChapter 2 coming soon:",
    [["Restart", game_start],
    ["Exit", sys.exit]])


approach_bushes_gameover.create_event(
    "You approach the bushes, head-in, unprepared, and start to regret your boldness. As you reflect on other terrible decisions of your past and how everything turned out just fine in the end, a vicious red-eyed rat jumps through the bushes and latches onto your neck. If only you had been more cautious and readied your sword. You try get the rat out of your neck, but its fangs are so deep into your neck that with every pull you're just helping the rat rip through your throat even faster.\nYou die.\n\n**GAME OVER**",
    [["Restart", game_start],
    ["Exit", sys.exit]])

trust_gut_gameover.create_event(
    "Good good, you're one step closer to learning the truth",
    [["Restart", game_start],
    ["Exit", sys.exit]])

restart_game.create_event(
    "You died:",
    [["Restart", game_start],
    ["Exit", sys.exit]])
