from random import randint, choice


def isLucky(chance_percent=50):
    if randint(1, 1000) <= chance_percent*10:
        return True
    return False


def create_transaction(client, user, trans_type=1, is_lead=False, url_from_override=None):
    transaction = dict(
        LogTime=user.date.strftime("%Y-%m-%d %H:%M:%S"),
        TransactionType=trans_type,
        CookieID=user.id,
        CookiesEnabled=True,
        ClientSite=client.name,
        TrackingSetup=client.trans_setup)

    media = banner = id_logpoints = logpoint_name = campaign= urlfrom = urlto = None

    if trans_type != 100:
        media = choice(client.medias)
        banner = choice(client.banners)
        campaign = choice(client.campaigns)

    else:
        id_logpoints = 1001 if is_lead else randint(1, 100)
        urlfrom = "www." + client.name + ".com/"
        urlto = urlfrom + "thankyou" if is_lead else urlfrom + "somepage"
        logpoint_name = "Thank you!" if is_lead else "some logpoint name"

    transaction["Media"] = media
    transaction["Banner"] = banner
    transaction["ID_LogPoints"] = id_logpoints
    transaction["URLto"] = urlto
    transaction["URLfrom"] = urlfrom
    transaction["LogPointName"] = logpoint_name
    transaction["Campaign"] = campaign

    if url_from_override is not None:
        transaction["URLfrom"] = url_from_override

    user.incr_date(weak=True if trans_type == 100 else False)

    return  transaction


def create_logpoint_chain(client, user, url_from_override=None):
    tlist = [create_transaction(client, user, trans_type=100, url_from_override=url_from_override)]
    while True:
        if isLucky(10):
            # Get lead
            tlist.append(create_transaction(client, user, trans_type=100, is_lead=True))
            break
        elif isLucky(80):
            # Another log
            tlist.append(create_transaction(client, user, trans_type=100))
        else:
            break
    return tlist
