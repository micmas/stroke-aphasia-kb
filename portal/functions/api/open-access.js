import {serveOpenAccess} from '../../lib/open-access.js';
export const onRequest=({request,env})=>serveOpenAccess(request,env.PDFS);
