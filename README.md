This Python code illustrates how Large Language Models / generative AI works, but using a
transparent algorithm instead of deep learning and neural nets. It builds lists of digraphs
and trigraphs found in the input file, and then generates sentences from a starter-word
using the probabilities of the digraphs (first-order model) and trigraphs (second-order model).

Subjectively the second-order output will be "better" (more like real English text) than
the first-order output, but try it for yourself and find out! Better yet, try to make a
third-order model yourself and see how much better it gets.

Actual Large Language Models train on a lot more data, and have a lot more context available.
They produce much better output than do these simple examples, but are ultimately driven by
statistics much as are these simple examples.

Sample run:

```
Enter source text file name: wuthering_heights.txt

First-order variations on 'this':
 this threat being , i’m used to go if she coughed troublesomely sometimes more , and strode to myself on my own mind owning my great thaw winds , had edgar linton ” “ and we saw us.
 this is this?
 this library , i gave the many-weeks’ deserted parlour ; but i took the mischief.
 this suffering , she pleaded eloquently for trifles bought for a lamb ; and held a child’s sensations flowed into tears : he saw an old lady to arrange her eyes ; the door with the moors of a predicament which awaited her manners.
 this moment that they wish to and thought ; and lower fruit had occasioned by the hour in winter , weeping was invisible : she’ll be comfortably asleep , for a blank , too.
 this grim aspect was never forgive myself!
 this speech , that joseph were erected and then we’s hear?
 this.
 this threat ; it ; commending catherine earnshaw_ , meantime , but immediately , i knew of mortification and i pitied you could not be altered?
 this exclamation was able to avoid delay.

Second-order variations on 'this':
 this room desperate.
 this week ; and between them.
 this arrangement ; and i watched and felt like ice.
 this , however , it seems a weary number of falls i’ve had many a time through wind and suffocating snow.
 this very morning ; and , as i , as she expressed it.
 this preparation was probably for our excursion till the beast , and his thick flaxen curls , felt his slender arms and his countenance suggested that idea.
 this revelation of his good humour ; so , is it half-an-hour now , ” she once was , when they are married , to disengage herself from linton’s arms.
 this penance.
 this minute , bearing a basin of coffee before him?
 this house that i would not chase me over the heights , and his large languid eyes — his wife and himself : at any part of her cousin , and mutter , “ the dogs gave notice of my accursed — of that.

First-order variations on 'precincts':
 precincts of doing his to inspect the whey-faced , if he heard him so diabolical at last , and devour the said i think _ was_ under this to any more a little what a forlorn hope you’ll go to miss!
 precincts of the cold nor locks from my eyes full benefit ; “ read in his mug ; but he’s swopped wi’ sich careless of the truth were limited to bend towards it right : i could not a motion to marry him all the kitchen hearth , “ ‘ gaumless , somebody else.
 precincts of my request?
 precincts of us into his kin beneath : it spontaneously at once , and whinstone.
 precincts of conjuring up here?
 precincts of his sister marrying aunt isabella emptied her coming.
 precincts of this side of perspicacity to be only joseph calls you bring another servant grow so you!
 precincts of a small inclination is accustomed to bid you are going to her word to the window.
 precincts of the “ and glanced at least , knowing whether she was now , the house , was half sneeringly , and down there yet she has claimed and the whole assembly , and i scolded the village?
 precincts of hot fire : her memory , we’ve noa _ you being unacceptable.

Second-order variations on 'precincts':
 precincts of the early trees smitten and blackened.
 precincts of the pulpit , which it was that , he became for some oranges , and placed him on purpose to distress us both , after a step to comfort her.
 precincts of the house would be in an elevated hollow , and , that he had doted on both sides of the morning , for the way they go the length of the settle , when i walked as if she comes in.
 precincts of the discarded ones , not to be an every-day spectacle.
 precincts of the coals.
 precincts of the kirkyard , where i made way for him : and your mother , perhaps , if you’ll only be in at every meal edgar was taken with a piece of crust , the storm in a corner of her hands , and now , ” she replied.
 precincts of the speaker came forward eagerly to greet me , but never mind mr.
 precincts of the little girl ; and she prattled to catherine.
 precincts of the grange.
 precincts of the exterior of his arm’s shadow , dashing a tear from his bed at five ) — “ i didn’t tell him , intimating that mr.

First-order variations on 'truth':
 truth were at work.
 truth of their company ; and despised me you , ” i once more of my heart!
 truth , but why , referring us , hareton was outrageous , master also , or announcing that for that occasion of this grieved , with her to send for i wondered much of swallowing her in fact , and wood.
 truth , ellen.
 truth , slowly drew no desire to the bran came to an expression of a bible near the path , without being covered her plenty.
 truth , dog.
 truth at length of a usurper of harshness?
 truth about to her , and mantle , and drink here , and he pushed the former self , or whatever i had just as big as she seized another ; so happy when she was too ; yet a plentiful evening , i dragged me her lids to speak , good-looking in thinking of mr.
 truth ) , but i refused remaining with any footmarks under the settle somewhere!
 truth of chipping off the gate.

Second-order variations on 'truth':
 truth , now venturing conjectures as to your money , ” he sobbed , as i quitted the apartment and furniture would have me under the influence of cold , at least return in a fortnight , according to custom.
 truth , ” answered the boy , than begin on mr.
 truth : i despatched emissaries down this path , and cheer my solitude ; the brows lowering , the more for his re-entrance ; and thrushcross grange — not if i were dead , he did not protract his stay beyond midnight.
 truth , were you?
 truth : do , ’ showed me her mother’s when a child take up before ; and while they exchanged caresses i took hold of her chair , a peculiar look of aversion , that my — ” he remarked , putting the master will inform you catherine linton is all i have not white blood.
 truth of her former home ; but , perhaps , for catherine’s soul to haunt him.
 truth , heathcliff!
 truth : do , now , darling child , hush!
 truth and not encourage my son to pass.
 truth , were never visible — still she did not know whether it was morning ; and above us.

First-order variations on 'once':
 once our heifers ; though i was a chapel , i’ve sometimes came upon a pail of all.
 once been sung you contradict your prying at the house-door ; “ why did not , decided that apartment , and that i have you?
 once as if her silent room , but , ” said the kitchen , “ ‘ no gratification at everybody ; for a woman laughed and my salvation , sincerely she would not only get rid of firing the world to the ruffianly child.
 once , he being gentry ; but it?
 once ; and get them.
 once more had seen her jailor : “ you cherishing the dead and i cannot tell him , sinking back my ear.
 once in.
 once , will not one knee.
 once in rapid glance down with him down , indeed , ’ he detests me.
 once.

Second-order variations on 'once':
 once : unspeakably consoled.
 once ; and besides , he generously returned.
 once to ask whether she will go wilfully wrong ; by that means , it is your last ride , when i had been mad enough to make an apology , and , benumbed to my place , ” she repeated.
 once , and when i left her husband : _ i’m_ no coward.
 once in twenty-four hours after the struggle , he does his best to speak to me than she had a bible in your life before?
 once or twice , or i’ll ask your abduction as a spaniel might which suspected the person who saw her , as he spoke in the kitchen , in my walk on the rails to listen to your old friend hindley , and a kind heart , maister , i’d expire with a relish this evening , ” she continued ; “ she’ll never be able to support itself through fatigue ; and yet a connection with the party , and take me on the floor , and half buried in heath ; edgar and cathy , imagining she would admit none of that kind that will be dark in ten minutes , but forgotten.
 once more.
 once that i know ; but happily my master , i thought i was moved with a black lock of his commendations , and readily found among my house of her delight.
 once in your hands out of doors , ” he said ; ‘ and scarcely swallowed a mouthful to her husband’s knee , and look rather more than once , ” he lifted the letter by a mingled sense of his countenance.
 once , but you should not be called the first day or two he re-entered , when he would be the most ordinary would be glad to observe , in the world as if she thought that her darlings might be partially removed by a blow that filled both eyes with water.

First-order variations on 'heathcliff':
 heathcliff fixed , and still preserving my own stall ; which retain the master had not call him some of those hills.
 heathcliff , i see a larch , with the skirts of kenneth , the carving-knife , and called out a clever scholar in avoiding both.
 heathcliff , and patient , you won’t let her chamber she experienced rough weather he wrote.
 heathcliff bid her almost gone.
 heathcliff looked just like devil’s name of abuse , they had he generously to bolt — was that he would it in our heifers ; and ordered?
 heathcliff!
 heathcliff , there since early autumn : his library ; they are they be , not expect.
 heathcliff.
 heathcliff was wrong!
 heathcliff , he growled hareton never endeavoured to obviate the room where did , “ answer!

Second-order variations on 'heathcliff':
 heathcliff , more than angered me.
 heathcliff.
 heathcliff!
 heathcliff termed a “ vulgar young ruffian , ” exclaimed catherine , coupled with some wild term of endearment or suffering ; and i had a long while.
 heathcliff was _ i_ should hate them all stand off , and i cannot eat or drink here , wife!
 heathcliff , muttering an echo of curses , which has taught me wisdom ; and , at this fantastic preference.
 heathcliff has your permission to continue writing at intervals of six or seven yards , a matronly lady , closing his lids , as early as possible , ” i replied.
 heathcliff!
 heathcliff!
 heathcliff ” : it can’t be scorned for seeking her good-will any more than mine.
```
