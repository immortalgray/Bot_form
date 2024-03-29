list_form = [
    {
        "question": "1. У вас был день, полный неудач и разочарований. Как проведёте вечер?",
        'answers': {
            1: 'Позвоню друзьям и позову их куда-нибудь, вместе горести переживать веселее.',
            2: 'Побуду наедине с собой: включу любимый сериал, наготовлю вкусняшек'
        }
    },
    {
        "question": "2. Вы пришли к психологу. Он задаёт вопрос: «Какое из двух утверждений описывает вас точнее?»",
        'answers': {
            1: 'Предпочитаю жить настоящим: для меня важно то, что происходит здесь и сейчас.',
            2: 'Частенько витаю в облаках: люблю мечтать и строить великие планы на будущее.'
        }
    },
    {
        "question": "3. Вам предложили переехать в мегаполис. Теперь вы в раздумьях. В крупном городе"
                    " больше возможностей, зато там, где вы живёте сейчас, ваши близкие и уютный дом."
                    " Как будете принимать непростое решение?",
        'answers': {
            1: 'Порыскаю в интернете, рассчитаю примерный бюджет на переезд. '
               'Тщательно взвешу все за и против, потом приму решение.',
            2: 'Сделаю так, как велит мне сердце. Интуиция меня никогда не подводила'
        }
    },
    {
        "question": "4. Через месяц у вас долгожданный отпуск, ура! Как к нему готовитесь?",
        'answers': {
            1: 'Подготовлюсь ко всему заранее и сделаю план по покорению достопримечательностей.',
            2: 'За пару часов до полёта закину в чемодан всё необходимое, '
               'а о достопримечательностях поспрашиваю у местных.'
        }
    }
]

list_character = {
    'ESTJ': 'Вы — руководитель\n'
            'Трудолюбие и целеустремлённость — ваши лучшие качества. '
            'Вы обожаете порядок, умеете и любите планировать, '
            'без опаски берётесь за самые сложные задачи, '
            'потому что уверены в успехе. '
            'Вам свойственен рациональный взгляд на вещи, '
            'фактам вы доверяете куда больше, чем ощущениям. '
            'Вы веселы, добродушны и любите компанию. '
            'Благодаря организаторским талантам вы без труда '
            'можете подбить окружающих на любую авантюру.',

    'ENTJ': 'Вы — командир\n'
            'Вы всегда на гребне волны: знаете всё о свежих трендах и тенденциях. '
            'Вам не занимать смелости, вы любите рисковать и '
            'всегда открыты новому. Вы динамичны, продуктивны и обожаете преодолевать '
            'сложности. Вся ваша жизнь — борьба во имя достижения заветной цели. '
            'У вас превосходные лидерские качества: харизма, авторитетность и '
            'умение мыслить стратегически притягивают к вам людей.',

    'ENFJ': 'Вы — наставник\n'
            'Вы очень проницательны: доверяете интуиции, и она никогда вас не подводит. '
            'Вы наблюдательны, испытываете неподдельный интерес к людям и их эмоциям, '
            'способны улавливать малейшие перемены настроения. Окружающие часто обращаются '
            'к вам за советом и поддержкой, а вы всегда рады им помочь, а иногда и вдохновить.',

    'ESFJ': 'Вы — энтузиаст\n'
            'Вы отлично ладите с людьми, всегда готовы прийти на помощь, иногда даже во вред '
            'собственным интересам. Вы отзывчивы и открыты. Любите и цените похвалу, '
            'одобрение окружающих необходимо вам как воздух. Если где-то возникает конфликт, '
            'вы чувствуете себя не в своей тарелке и пытаетесь любой ценой восстановить мир и '
            'гармонию. Вы как лучик света в тёмном царстве — способны заряжать людей позитивом '
            'и вести за собой.',

    'ENTP': 'Вы — изобретатель\n'
            'Таких, как вы, часто называют идейными вдохновителями. Вы любопытны, мобильны, '
            'обожаете быть в движении и легко приспосабливаетесь к переменам. Вы — настоящий '
            'генератор идей, постоянно что-то изобретаете и подвергаете сомнению. Вы ненавидите '
            'рутину и всеми силами стремитесь её избегать. Вас пленит новое и неизведанное, '
            'поэтому вы часто меняете увлечения. Вы считаете, что в жизни нужно попробовать '
            'если не всё, то многое.',

    'ESTP': 'Вы — непоседа\n'
            'Вас отлично описывает фраза: «Вижу цель — не вижу препятствий». Вы стремитесь к '
            'победе любой ценой, сметая на своём пути все преграды. Вы решительны и дерзки, '
            'живёте моментом и любите быть в центре внимания. Жажда жизни в вас так и кипит, '
            'вы стремитесь всё познавать на практике и не терять ни одной ценной минуты.',

    'ENFP': 'Вы — чемпион\n'
            'Вы — творческая личность с неуёмной фантазией и отличным воображением. '
            'Вы открыты миру, свободолюбивы, стрессоустойчивы и не боитесь перемен. '
            'Вам важно постоянно проявлять инициативу, предлагать оригинальные решения, '
            'активно взаимодействовать с людьми и сопереживать им. Рутинные задачи для '
            'вас — сущая пытка и наказание.',

    'ESFP': 'Вы — политик\n'
            'Вы живёте сегодняшним днём и получаете огромное удовольствие от сиюминутных '
            'наслаждений. Планирование и разработка стратегий вас утомляют. Делая что-нибудь, '
            'вы часто полагаетесь на удачу, а в случае поражения бросаете работу не закончив. '
            'Вы спонтанны и непредсказуемы, ненавидите проволочки и стремитесь получать '
            'всё и сразу. Вы любите производить впечатление на окружающих и заводить '
            'полезные знакомства.',

    'ISTJ': 'Вы — администратор\n'
            '«Семь раз отмерь, один раз отрежь» — это про вас. Вы любите строгость и порядок, '
            'тщательно продумываете и анализируете свои действия. Вы нацелены на результат, '
            'поэтому берётесь только за те задачи, которые точно сможете выполнить. '
            'Вы аккуратны и терпеливы, не любите пустой болтовни. Вы цените честность и '
            'трудолюбие, а попытки увильнуть от ответственности вызывают у вас такое же '
            'негодование, как и плохо выполненная работа.',

    'INTJ': 'Вы — стратег\n'
            'Вы независимы, эрудированны и умеете грамотно расставлять приоритеты. '
            'Вы не любите шумные компании, а вдохновение и прорывные идеи черпаете внутри себя. '
            'Вы перфекционист до мозга костей, а ваша заветная мечта — сделать окружающий мир '
            'более совершенным. Вы ненавидите ретроградные правила и глупые ограничения и '
            'стараетесь бороться с ними при помощи своих инновационных задумок, '
            'в чём нередко преуспеваете.',

    'INFJ': 'Вы — гуманист\n'
            'Помощь окружающим для вас — неотъемлемая часть жизни. Вы верите, что мир могут '
            'спасти любовь и сострадание. Если кому-то из ваших близких потребуется помощь, '
            'то он точно обратится именно к вам, а в ответ всегда получит чёткое руководство '
            'к действию. Вы ранимы, цените верность и не прощаете предательства.',

    'ISFJ': 'Вы — защитник\n'
            'Вы чуете фальшь за версту, поэтому держите чужих на расстоянии, а за близких '
            'стоите горой. Вы делаете всё, чтобы дорогие вам люди были счастливы, и каждый '
            'день стараетесь приятно их удивить. Вы усердны, для исполнения целей часто '
            'прикладываете неимоверные усилия. Правда, бываете неторопливы и любите '
            'откладывать на потом. Несмотря на это, на вас можно положиться, потому что вы '
            'никогда не забрасываете то, что начали.',

    'INTP': 'Вы — архитектор\n'
            'У вас философский склад ума. Вы постоянно выдвигаете гипотезы, спорите '
            'сами с собой, подмечаете важные детали и стремитесь докопаться до сути '
            'вещей. Со стороны это выглядит так, будто вы рассеянны и витаете в облаках. '
            'Отчасти это верно: бытовые вопросы вас нисколько не волнуют. Вы сосредоточены '
            'на важных размышлениях и особого интереса к окружающим не испытываете. '
            'Вы цените уют и комфорт, а к переменам относитесь крайне негативно.',

    'ISTP': 'Вы — виртуоз\n'
            'Вы познаёте мир через ощущения, способны глубоко сопереживать людям и '
            'цените искренность. Вы достаточно открыты, но в случае лжи или лицемерия '
            'уходите в себя. Вы тщательно продумываете каждый шаг, прежде чем сделать '
            'что-нибудь. Вы пунктуальны, объективны и в меру любопытны.',

    'INFP': 'Вы — лирик\n'
            'Смысл жизни для вас — гармония с собой и окружающим миром. '
            'Вы впечатлительная натура и остро реагируете на любую несправедливость. '
            'Для вас важно самовыражение: вы не только проводите грандиозную работу над '
            'своим внутренним миром, но и не забываете о внешности. Вы бываете мечтательны '
            'и погружены в себя, но всегда находите возможность уделить внимание близким.',

    'ISFP': 'Вы — композитор\n'
            'Вы тот самый редкий человек, которого не страшит рутина и однообразие. '
            'Вы принимаете мир таким, какой он есть, не стремитесь его менять и '
            'подстраивать под себя. Вы просто живёте в своё удовольствие, наслаждаясь '
            'тем, что уже имеете. Вы не стремитесь никем руководить и командовать. '
            'Вы то самое надёжное плечо, на которое можно опереться и не ждать подвоха.'
}
